# Installation — prototype de traduction française

**État : test uniquement, pas de version finale.**

## Option A — ZIP depuis GitHub Actions

La [construction automatisée](../../actions/workflows/build-test-pak.yml) vise à créer un artefact nommé `NuclearNightmare-FR-TEST`. Si la construction aboutit :

1. Télécharger l'artefact ZIP depuis l'exécution GitHub Actions.
2. Extraire le ZIP interne `NuclearNightmare-FR-TEST.zip` et lire `SHA256SUMS.txt`.
3. Copier le dossier `NuclearNightmare` du ZIP dans le dossier principal du jeu, sans remplacer le fichier original `NuclearNightmare-Windows.pak`.
4. Sélectionner **Russe** dans les paramètres (la traduction remplace provisoirement ce choix).

Le seul fichier ajouté est `NuclearNightmare/Content/Paks/NuclearNightmare-FR_P.pak`.

## Option B — construire le patch sur Linux Bazzite

Dans le dossier du dépôt cloné :

```bash
bash tools/construire_pak_test.sh "$HOME/NuclearNightmare_Traduction.tar.gz"
```

*Le constructeur nécessite `repak` installé dans `$HOME/.local/opt/repak/` ou présent dans `PATH`, ainsi que les fichiers source que vous avez vous-même extraits de votre copie du jeu.*

Pour l'option B, placez les fichiers CSV et `construire_fr_locres.py` dans le même dossier que le script si vous utilisez le kit ZIP plutôt que la disposition du dépôt. Le résultat apparaît sous `dist-test/NuclearNightmare-FR-TEST.zip`.

## Désinstallation

Supprimer uniquement `NuclearNightmare-FR_P.pak`, puis relancer le jeu.

## Limites

Le chargement du mod et le remplacement du choix de langue russe **ne sont pas confirmés par un test dans le jeu**. Le patch n'est pas un programme, ne contient aucun `.exe` et ne modifie pas l'archive de base.
