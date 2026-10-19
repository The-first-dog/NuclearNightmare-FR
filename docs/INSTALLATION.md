# Installer la traduction française de Nuclear Nightmare

> ⚠️ **Cette installation n'a pas encore été validée en jeu. Il n'existe actuellement aucune Release prête pour le public.** Ce guide décrit le fonctionnement prévu et sera ajusté après les premiers tests.

## 1. Télécharger le bon fichier

Une fois disponible, ouvrez la page [Releases](https://github.com/The-first-dog/NuclearNightmare-FR/releases) et récupérez **le ZIP de traduction**, et non les liens automatiques `Source code (zip)` / `Source code (tar.gz)` de GitHub.

Le ZIP devra contenir :

```text
NuclearNightmare/
└── Content/
    └── Paks/
        └── NuclearNightmare-FR_P.pak
```

L'utilisateur n'aura aucun logiciel à installer ni programme à exécuter.

## 2. Trouver le dossier du jeu

**Sur Windows ou Linux avec Steam/Proton :**

1. Ouvrez **Steam → Bibliothèque**.
2. Faites un clic droit sur **Nuclear Nightmare**.
3. Choisissez **Propriétés → Fichiers installés → Parcourir** (le libellé peut varier légèrement selon la version de Steam).
4. Le dossier racine du jeu s'ouvre. Il devrait notamment contenir **`NuclearNightmare.exe`** sur la version Windows.

Cette méthode évite de devoir deviner le chemin du dossier Steam.

## 3. Copier la traduction

1. Décompressez le ZIP de traduction.
2. Copiez son dossier **`NuclearNightmare`** dans le dossier racine du jeu ouvert précédemment.
3. Acceptez la **fusion des dossiers** si Steam ou le gestionnaire de fichiers le propose.
4. Le fichier suivant doit se trouver à cet emplacement :

```text
NuclearNightmare/Content/Paks/NuclearNightmare-FR_P.pak
```

**Ne supprimez ni ne remplacez** `NuclearNightmare-Windows.pak`.

## 4. Choisir la langue

Pour le **prototype de test**, le patch est conçu pour remplacer les ressources de la **langue russe**. Après démarrage du jeu, choisissez donc **Russe** dans le menu des langues. Cela ne garantit pas encore que le patch sera chargé : ce point doit être testé.

## 5. Désinstaller ou revenir à la version originale

Fermez le jeu, supprimez uniquement **`NuclearNightmare-FR_P.pak`** du dossier **`NuclearNightmare/Content/Paks/`**, puis relancez le jeu.

Si le jeu pose problème, vous pouvez également utiliser dans Steam **Propriétés → Fichiers installés → Vérifier l'intégrité des fichiers du jeu**. Cette vérification peut restaurer les fichiers officiels ; elle ne retire pas nécessairement les fichiers supplémentaires ajoutés manuellement.

## 6. Signaler un problème

Ouvrez une [Issue](https://github.com/The-first-dog/NuclearNightmare-FR/issues) avec la version du jeu, une capture d'écran et une courte description.

### Pour les testeurs et mainteneurs seulement

Le projet comprend un [workflow de construction du patch](https://github.com/The-first-dog/NuclearNightmare-FR/blob/main/.github/workflows/build-test-pak.yml) et des [scripts](https://github.com/The-first-dog/NuclearNightmare-FR/tree/main/tools). Ce matériel ne remplace pas un ZIP de Release testé ; les artefacts GitHub Actions peuvent nécessiter une connexion et expirer.

La traduction est un projet de fans indépendant. Une copie officielle du jeu est nécessaire.
