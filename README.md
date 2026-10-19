# Nuclear Nightmare — Traduction française 🇫🇷

Traduction française **non officielle** de **Nuclear Nightmare**, créée par **FantinHD**.

Ce projet vise à rendre le jeu accessible en français, avec une installation simple : **un fichier `.pak` à copier, sans exécutable ni installateur**.

## 📥 Télécharger la traduction

> ⚠️ **Version en préparation — aucun patch validé dans le jeu n'est encore disponible au téléchargement.**

Les **1 463 entrées de localisation** disposent déjà d'une proposition française. Nous terminons la relecture et les essais techniques du patch.

➡️ [Consulter les versions disponibles (Releases)](https://github.com/The-first-dog/NuclearNightmare-FR/releases) — *aucune version publiée pour le moment*.

**Ne téléchargez pas le code source du dépôt en pensant installer la traduction : il ne s'agit pas du patch.**

## 🇫🇷 Contenu traduit

- Menus et interface
- Paramètres et commandes
- Objectifs et notifications
- Objets, équipements et compétences
- Messages de jeu et descriptions
- Textes de localisation supplémentaires présents en russe

**État actuel :** 1 463 / 1 463 entrées proposées en français. Certaines phrases doivent encore être revues dans leur contexte et tous les textes de l'interface ne sont pas nécessairement stockés dans ces fichiers.

## 📦 Comment installer la traduction ?

*Les étapes ci-dessous décrivent l'installation prévue du futur patch. Elles seront confirmées lors du test dans le jeu.*

1. Téléchargez **`NuclearNightmare-FR.zip`** depuis la rubrique **Releases**, une fois la première version publiée.
2. Dans **Steam**, faites un clic droit sur **Nuclear Nightmare** → **Propriétés** → **Fichiers installés** → **Parcourir**.
3. Ouvrez le ZIP et copiez le dossier **`NuclearNightmare`** dans le dossier principal du jeu.
4. Acceptez la **fusion des dossiers**, sans remplacer le fichier original **`NuclearNightmare-Windows.pak`**.
5. Lancez le jeu. **Pour la première version de test, sélectionnez « Russe »** dans les paramètres de langue : cette entrée servira provisoirement à afficher le français, *si le mod est correctement chargé*.

Le fichier ajouté sera :

```text
NuclearNightmare/
└── Content/
    └── Paks/
        ├── NuclearNightmare-Windows.pak     ← archive originale (ne pas toucher)
        └── NuclearNightmare-FR_P.pak         ← traduction française
```

📖 [Instructions détaillées et résolution de problèmes](docs/INSTALLATION.md)

## 🗑️ Comment désinstaller ?

Supprimez uniquement **`NuclearNightmare/Content/Paks/NuclearNightmare-FR_P.pak`** puis relancez le jeu. Vous ne devriez pas avoir besoin de réinstaller le jeu.

## 🔒 Transparence et sécurité

- Aucun programme `.exe`, aucune modification du jeu original.
- Le futur téléchargement contiendra seulement le patch `.pak` et des instructions.
- Le projet est consultable sur GitHub ; les versions seront accompagnées d'une empreinte SHA-256.
- **Compatibilité non encore confirmée** : aucune promesse que le mod fonctionne tant que le test en jeu n'est pas terminé.
- Une **copie légitime du jeu** est nécessaire.

## 💬 Un problème de traduction ?

Vous pouvez [ouvrir une Issue sur GitHub](https://github.com/The-first-dog/NuclearNightmare-FR/issues) avec une capture d'écran, le texte à corriger et la version du jeu.

## 🛠️ Pour les contributeurs

Les fichiers de traduction et outils se trouvent dans ce dépôt :

- [Tableau des traductions](translations/NuclearNightmare_traduction_FR.csv)
- [Suivi de l'avancement](docs/AVANCEMENT.md)
- [Scripts et ressources de construction](tools/)
- [Fichier de construction du patch de test](.github/workflows/build-test-pak.yml)

Ces fichiers techniques **ne sont pas nécessaires** pour installer une future version publique.

## 👤 FantinHD

▶️ [YouTube](https://www.youtube.com/@TheFirstDog)  
🎮 [Mes jeux sur Google Play](https://play.google.com/store/apps/dev?id=8088754359282570640)

---

*Projet de fans non officiel et sans but lucratif. Aucun lien avec les développeurs ou éditeurs de Nuclear Nightmare. Tous les droits sur le jeu appartiennent à leurs ayants droit respectifs.*
