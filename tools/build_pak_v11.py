#!/usr/bin/env python3
"""Small, standalone Unreal Pak V11 writer for a single uncompressed resource.

Conforms to the field layout of UnrealPak V11 (FNV64 path-hash index).
No source assets are modified. Intentionally avoids third-party executables.
Use `repak info/list/get` as an independent validation when available.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import struct
import zipfile

MASK=(1<<64)-1
ENTRY='NuclearNightmare/Content/Localization/Game/ru/Game.locres'
MOUNT='../../../'
SEED=0x42459304
MAGIC=0x5A6F12E1


def u32(n): return struct.pack('<I',n)
def i32(n): return struct.pack('<i',n)
def u64(n): return struct.pack('<Q',n)
def string(value):
    if value.isascii():
        return u32(len(value)+1)+value.encode()+b'\0'
    else:
        chars=value.encode('utf-16le')
        return i32(-(len(chars)//2+1))+chars+b'\0\0'


def fnv64_path(path,seed):
    h=(0xcbf29ce484222325+seed)&MASK
    for b in path.lower().encode('utf-16le'):
        h=((h^b)*0x100000001b3)&MASK
    return h


def write_pak(data,path,seed=SEED):
    out=io.BytesIO()
    data_hash=hashlib.sha1(data).digest()
    # FPackEntry for uncompressed resource: offset=0, compressed=size,
    # uncompressed=size, compression=0, SHA1, encryption=0, block size=0.
    out.write(u64(0)+u64(len(data))+u64(len(data))+u32(0)+data_hash+b'\0'+u32(0))
    out.write(data)
    index_offset=out.tell()
    # Encoded entry flags: 32-bit offset, size and uncompressed size.
    encoded=u32((1<<29)|(1<<30)|(1<<31))+u32(0)+u32(len(data))
    hash_index=u32(1)+u64(fnv64_path(ENTRY,seed))+u32(0)+u32(0)
    split=ENTRY.split('/')
    directories=['/']+['/'.join(split[:i])+'/' for i in range(1,len(split))]
    fdi=io.BytesIO()
    fdi.write(u32(len(directories)))
    for directory in sorted(directories):
        fdi.write(string(directory))
        if directory==('/'.join(split[:-1])+'/'):
            fdi.write(u32(1)+string(split[-1])+i32(0))
        else:
            fdi.write(u32(0))
    fdi=fdi.getvalue()
    # Primary index is immediately followed by path hash index and directory index.
    index_size=(len(string(MOUNT))+4+8+4+8+8+20+4+8+8+20+4+len(encoded)+4)
    phi_offset=index_offset+index_size
    dir_offset=phi_offset+len(hash_index)
    index=(string(MOUNT)+u32(1)+u64(seed)+
           u32(1)+u64(phi_offset)+u64(len(hash_index))+hashlib.sha1(hash_index).digest()+
           u32(1)+u64(dir_offset)+u64(len(fdi))+hashlib.sha1(fdi).digest()+
           u32(len(encoded))+encoded+u32(0))
    assert len(index)==index_size
    out.write(index+hash_index+fdi)
    footer=(b'\0'*16+b'\0'+u32(MAGIC)+u32(11)+u64(index_offset)+
            u64(len(index))+hashlib.sha1(index).digest()+b'\0'*(5*32))
    assert len(footer)==221
    out.write(footer)
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(out.getvalue())
    return {'resource':ENTRY,'version':11,'mount':MOUNT,'seed':f'{seed:08x}',
            'payload_size':len(data),'pak_size':path.stat().st_size,
            'pak_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'locres_sha256':hashlib.sha256(data).hexdigest()}


def verify_pak(path):
    b=Path(path).read_bytes(); footer=b[-221:]
    assert footer[:17]==b'\0'*17
    mg,ver,off,size=struct.unpack_from('<IIQQ',footer,17)
    assert (mg,ver)==(MAGIC,11)
    index=b[off:off+size]
    assert hashlib.sha1(index).digest()==footer[41:61]
    assert index[:len(string(MOUNT))]==string(MOUNT)
    at=len(string(MOUNT)); num,seed=struct.unpack_from('<IQ',index,at);at+=12
    assert num==1 and seed==SEED
    hp=struct.unpack_from('<IQQ',index,at);at+=20
    assert hp[0]==1
    assert hashlib.sha1(b[hp[1]:hp[1]+hp[2]]).digest()==index[at:at+20];at+=20
    hd=struct.unpack_from('<IQQ',index,at);at+=20
    assert hd[0]==1
    assert hashlib.sha1(b[hd[1]:hd[1]+hd[2]]).digest()==index[at:at+20];at+=20
    enlen,=struct.unpack_from('<I',index,at);at+=4
    flags,entry_offset,payload_size=struct.unpack_from('<III',index,at)
    assert (flags,entry_offset)==(0xe0000000,0) and enlen==12
    at+=12
    assert struct.unpack_from('<I',index,at)[0]==0
    phi=b[hp[1]:hp[1]+hp[2]]
    assert struct.unpack_from('<I',phi,0)[0]==1
    assert struct.unpack_from('<Q',phi,4)[0]==fnv64_path(ENTRY,seed)
    assert struct.unpack_from('<II',phi,12)==(0,0)
    locres=b[53:53+payload_size]
    assert len(locres)==payload_size and b[53+payload_size:off]==b''
    assert hashlib.sha1(locres).digest()==b[28:48]
    fdi=b[hd[1]:hd[1]+hd[2]]
    assert b'Game.locres\0' in fdi and struct.unpack_from('<I',fdi,0)[0]==6
    return locres


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('locres')
    parser.add_argument('output',help='NuclearNightmare-FR_P.pak output')
    parser.add_argument('--zip',help='Optional test ZIP with installation path')
    args=parser.parse_args()
    data=Path(args.locres).read_bytes()
    assert data[:16]==bytes.fromhex('0e147475674a03fc4a15909dc3377f1b'),'Not a LocRes'
    assert data[16]==3,'Unsupported LocRes version'
    info=write_pak(data,args.output)
    assert verify_pak(args.output)==data
    if args.zip:
        with zipfile.ZipFile(args.zip,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            z.write(args.output,'NuclearNightmare/Content/Paks/NuclearNightmare-FR_P.pak')
        with zipfile.ZipFile(args.zip) as z:
            check=z.read('NuclearNightmare/Content/Paks/NuclearNightmare-FR_P.pak')
            assert check==Path(args.output).read_bytes()
        info['zip_sha256']=hashlib.sha256(Path(args.zip).read_bytes()).hexdigest()
        info['zip_size']=Path(args.zip).stat().st_size
    print(json.dumps(info,ensure_ascii=False,indent=2))

if __name__=='__main__':main()