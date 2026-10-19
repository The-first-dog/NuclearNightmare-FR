# Installer la traduction française de Nuclear Nightmare

**Version candidate : v1.0.0 RC1** — installation simple par copie d'un fichier `.pak`.

## Télécharger

Téléchargez directement **[NuclearNightmare-FR-v1.0.0-rc.1.zip](https://github.com/The-first-dog/NuclearNightmare-FR/raw/refs/heads/main/downloads/NuclearNightmare-FR-v1.0.0-rc.1.zip)**. Le ZIP se trouve aussi dans le dossier `downloads/` du dépôt.

La page [Releases GitHub](https://github.com/The-first-dog/NuclearNightmare-FR/releases) peut proposer des versions automatisées. Évitez les archives intitulées « Source code » : ce ne sont pas les patches installables.

Le ZIP direct est une **version candidate** : son intégrité et sa structure sont vérifiées, mais son comportement dans chaque version du jeu n'est pas garanti.

## Installation sous Windows (Steam)

1. Fermez **Nuclear Nightmare**.
2. Ouvrez Steam → **Bibliothèque** → clic droit sur **Nuclear Nightmare** → **Propriétés** → **Fichiers installés** → **Parcourir**.
3. Décompressez le ZIP téléchargé.
4. Copiez le dossier `NuclearNightmare` extrait dans le **dossier principal du jeu** (là où se trouve `NuclearNightmare.exe`).
5. Autorisez la **fusion des dossiers**. Aucun fichier original ne doit être remplacé.
6. Vérifiez que le fichier ajouté est ici :

```text
NuclearNightmare/
└── Content/
    └── Paks/
        ├── NuclearNightmare-Windows.pak   (fichier original à conserver)
        └── NuclearNightmare-FR_P.pak       (fichier ajouté)
```

7. Démarrez le jeu et sélectionnez **Russe** dans les langues. Le patch utilise provisoirement cet emplacement pour le français.

## Désinstallation

Fermez le jeu. Supprimez **uniquement** `NuclearNightmare/Content/Paks/NuclearNightmare-FR_P.pak`, puis relancez le jeu.

## Résoudre un problème

- **Le français ne s'affiche pas :** vérifiez le chemin du `.pak`, la sélection « Russe » et la version du jeu.
- **Le jeu ne démarre plus :** supprimez le seul `.pak` ajouté, puis redémarrez.
- **Texte coupé ou mal traduit :** fournissez une capture dans les [Issues](https://github.com/The-first-dog/NuclearNightmare-FR/issues/new).
- **Linux / Steam Proton :** non validé pour cette version ; aucune compatibilité garantie.

### Vérification de l'intégrité du ZIP

Une empreinte SHA-256 est publiée avec l'archive dans `SHA256SUMS.txt`. Sous Windows, vous pouvez vérifier l'empreinte avec :

```powershell
Get-FileHash .\NuclearNightmare-FR-v1.0.0-rc.1.zip -Algorithm SHA256
```

La valeur affichée doit être égale à celle indiquée dans `SHA256SUMS.txt`.

## Précisions

Le patch est une traduction de fans non officielle, non associée aux créateurs du jeu. Il ne fournit aucun exécutable, seulement un `.pak` de localisation. Une copie originale du jeu est nécessaire.
