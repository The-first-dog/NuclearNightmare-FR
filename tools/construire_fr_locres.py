#!/usr/bin/env python3
"""Rebuild UE LocRes v3 with CSV French translations, never touches original game data.

Usage: python3 construire_fr_locres.py source.tar.gz traduction.csv fr/Game.locres
       python3 construire_fr_locres.py source.tar.gz traduction.csv fr/Game.locres --allow-incomplete
For the user's own game copy. This writes a locres, NOT an installable .pak or locale registration.
"""
import argparse, collections, csv, io, pathlib, re, struct, tarfile, sys

MAGIC=bytes.fromhex('0e147475674a03fc4a15909dc3377f1b')
TOKEN=re.compile(r'\{[^{}\r\n]+\}|%[0-9.]*[sdf]|<[^<>]+>')

class Reader:
    def __init__(self,b): self.b=io.BytesIO(b)
    def read(self,n):
        r=self.b.read(n)
        if len(r)!=n: raise ValueError('Truncated locres')
        return r
    def i32(self): return struct.unpack('<i',self.read(4))[0]
    def u32(self): return struct.unpack('<I',self.read(4))[0]
    def i64(self): return struct.unpack('<q',self.read(8))[0]
    def string(self):
        n=self.i32()
        if abs(n)>2_000_000: raise ValueError('Invalid UE string length')
        if n==0:return ''
        if n>0:
            b=self.read(n)
            if b[-1:]!=b'\0':raise ValueError('Invalid ASCII NUL termination')
            return b[:-1].decode('utf8')
        b=self.read(-n*2)
        if b[-2:]!=b'\0\0':raise ValueError('Invalid UTF-16 NUL termination')
        return b[:-2].decode('utf-16le')
    def key(self): return self.u32(),self.string()

def read_locres(b):
    r=Reader(b)
    if r.read(16)!=MAGIC: raise ValueError('Unsupported locres magic')
    version=r.read(1)[0]
    if version!=3: raise ValueError('Expected locres v3, got '+str(version))
    pool_offset=r.i64()
    declared=r.i32()
    nsnum=r.i32()
    namespaces=[]
    for _ in range(nsnum):
        ns_hash,ns=r.key(); count=r.i32();entries=[]
        for _ in range(count):
            key_hash,key=r.key();source_hash=r.u32();idx=r.i32()
            entries.append([key_hash,key,source_hash,idx])
        namespaces.append([ns_hash,ns,entries])
    if r.b.tell()!=pool_offset:raise ValueError('Unexpected pool offset')
    pool=[]; refcounts=[]
    for _ in range(r.i32()):
        pool.append(r.string());refcounts.append(r.i32())
    if r.b.tell()!=len(b):raise ValueError('Unexpected trailing bytes')
    if sum(len(ns[2]) for ns in namespaces)!=declared:raise ValueError('Key count mismatch')
    if sum(refcounts)!=declared:raise ValueError('Pool reference count mismatch')
    if any(e[3]>=len(pool) or e[3]<0 for ns in namespaces for e in ns[2]):raise ValueError('Bad string index')
    return namespaces,pool

def encode_string(s):
    if s.isascii():
        raw=s.encode('ascii')+b'\x00'
        return struct.pack('<i',len(raw))+raw
    raw=s.encode('utf-16le')+b'\x00\x00'
    return struct.pack('<i',-len(raw)//2)+raw

def write_locres(namespaces,pool):
    out=io.BytesIO()
    def i32(x):out.write(struct.pack('<i',x))
    def u32(x):out.write(struct.pack('<I',x))
    out.write(MAGIC+b'\x03')
    out.write(b'\x00'*8)
    count=sum(len(ns[2]) for ns in namespaces)
    i32(count);i32(len(namespaces))
    refcounts=[0]*len(pool)
    for ns_hash,ns,entries in namespaces:
        u32(ns_hash);out.write(encode_string(ns));i32(len(entries))
        for kh,key,sourcehash,index in entries:
            u32(kh);out.write(encode_string(key));u32(sourcehash);i32(index)
            refcounts[index]+=1
    off=out.tell()
    i32(len(pool))
    for s,c in zip(pool,refcounts):
        out.write(encode_string(s));i32(c)
    result=bytearray(out.getvalue())
    struct.pack_into('<q',result,17,off)
    return bytes(result)

def read_source(archive,language):
    with tarfile.open(archive,'r:gz') as tar:
        path=f'NuclearNightmare_Traduction/{language}/Game.locres'
        member=tar.extractfile(path)
        if member is None:raise ValueError('Missing '+path)
        return member.read()

def main():
    ap=argparse.ArgumentParser(description='Generate a draft French Unreal Engine locres from a completed CSV')
    ap.add_argument('archive',help='NuclearNightmare_Traduction.tar.gz')
    ap.add_argument('csv',help='NuclearNightmare_traduction_FR.csv (UTF-8)')
    ap.add_argument('output',help='output Game.locres path')
    ap.add_argument('--ru-overrides',help='CSV de variantes françaises pour les chaînes russes divergentes')
    ap.add_argument('--allow-incomplete',action='store_true',help='Build an INCOMPLETE test file with fallback languages')
    args=ap.parse_args()
    en_b=read_source(args.archive,'en');ru_b=read_source(args.archive,'ru')
    en_ns,en_pool=read_locres(en_b);ru_ns,ru_pool=read_locres(ru_b)
    assert write_locres(en_ns,en_pool)==en_b,'English round trip mismatch; rebuild blocked'
    assert write_locres(ru_ns,ru_pool)==ru_b,'Russian round trip mismatch; rebuild blocked'
    en_map={(name,key):(src_hash,en_pool[idx]) for _,name,entries in en_ns for _,key,src_hash,idx in entries}
    ru_map={(name,key):(src_hash,ru_pool[idx]) for _,name,entries in ru_ns for _,key,src_hash,idx in entries}
    with open(args.csv,'r',encoding='utf-8-sig',newline='') as f:
        csv_rows=list(csv.DictReader(f))
    user={(r['Namespace'],r['Cle']):r for r in csv_rows}
    if len(user)!=len(csv_rows):raise ValueError('Duplicate CSV keys')
    expected=set(en_map)|set(ru_map)
    if set(user)!=expected:raise ValueError('CSV missing/extra keys, refusing to build')
    missing=[k for k in expected if not user[k]['Francais'].strip()]
    if missing and not args.allow_incomplete:
        raise ValueError(f'{len(missing)} French translations still blank; use --allow-incomplete ONLY for tests')
    ru_overrides = {}
    if args.ru_overrides:
        with open(args.ru_overrides, 'r', encoding='utf-8-sig', newline='') as rf:
            for override in csv.DictReader(rf):
                k = (override['Namespace'], override['Cle'])
                if k in ru_overrides: raise ValueError('Duplicate RU override '+repr(k))
                if k not in ru_map: raise ValueError('Unknown RU override '+repr(k))
                if k not in user: raise ValueError('Missing master entry for RU override '+repr(k))
                original = ru_map[k][1]
                translated = override['Francais_RU']
                if not translated.strip(): raise ValueError('Empty RU override '+repr(k))
                if sorted(TOKEN.findall(original)) != sorted(TOKEN.findall(translated)):
                    raise ValueError('Placeholders changed in RU override '+repr(k))
                ru_overrides[k] = translated
    new_ns=[]; text_pool=[]; index={}
    def add(s):
        if s not in index:index[s]=len(text_pool);text_pool.append(s)
        return index[s]
    ordered_ns={n:(hash_,[]) for hash_,n,_ in ru_ns}
    for hash_,n,entries in en_ns:
        if n not in ordered_ns:ordered_ns[n]=(hash_,[])
    # Prefer Russian reference hashes where source versions conflict; these may need review in-game.
    for ns in [n for _,n,_ in ru_ns] + [n for _,n,_ in en_ns if n not in {x[1] for x in ru_ns}]:
        ns_hash=ordered_ns[ns][0]; entries=[]
        ru_entries={e[1]:e for _,n,es in ru_ns if n==ns for e in es}
        en_entries={e[1]:e for _,n,es in en_ns if n==ns for e in es}
        for key in sorted(set(ru_entries)|set(en_entries)):
            k=(ns,key); r=user[k]; fr=r['Francais']
            source= r['Anglais'] or r['Russe']
            if fr and sorted(TOKEN.findall(source))!=sorted(TOKEN.findall(fr)):
                raise ValueError('Placeholders changed for key '+key)
            fallback=r['Anglais'] or r['Russe']
            string=ru_overrides.get(k, fr if fr.strip() else fallback)
            entry=ru_entries.get(key, en_entries.get(key))
            entries.append([entry[0],key,entry[2],add(string)])
        new_ns.append([ns_hash,ns,entries])
    b=write_locres(new_ns,text_pool)
    target=pathlib.Path(args.output)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(b)
    parsed,pool=read_locres(b)
    assert sum(len(x[2]) for x in parsed)==len(expected)
    print(f'Created: {target} ({len(expected)} keys, {len(missing)} incomplete translations, {len(ru_overrides)} RU semantic overrides)')
    print('Note: this is NOT an installable mod; it still needs registration of the French culture and packaging.')

if __name__=='__main__':
    try: main()
    except (OSError,ValueError,AssertionError,KeyError) as e:
        print('ERROR:',e,file=sys.stderr);sys.exit(1)