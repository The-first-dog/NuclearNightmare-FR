# Nuclear Nightmare — Traduction française non officielle

> **Projet en cours de test : aucune version finale publiée.** La première passe française couvre **1 463 / 1 463 entrées** ; une relecture complète et le test dans le jeu restent indispensables.

Traduction française communautaire de **Nuclear Nightmare** (Unreal Engine). Projet indépendant de fans, non affilié aux développeurs.

## État

| Indicateur | Valeur |
|---|---:|
| Clés de localisation | **1 463** |
| Propositions françaises | **1 463 / 1 463** |
| Brouillons à relire | **1 443** |
| Brouillons à vérifier prioritairement dans le jeu | **9** |
| Textes révisés manuellement | **11** |
| Entrées EN/RU aux hashes différents | **92** |
| Traductions spécifiques à la source russe | **11** |
| Compilation du fichier `.locres` | **Réussie et relue par le parseur** |
| Compatibilité dans le jeu | **Non testée** |

**100 % de couverture n'équivaut pas à 100 % de qualité vérifiée.**

## Fichiers

- [Traduction principale (CSV)](translations/NuclearNightmare_traduction_FR.csv)
- [Variantes du texte russe (CSV)](translations/NuclearNightmare_traduction_RU_overrides.csv)
- [Reconstruction du LocRes](tools/construire_fr_locres.py)
- [Construction locale du patch .pak de test (Bazzite)](tools/construire_pak_test.sh)
- [État des travaux](docs/AVANCEMENT.md)
- [Installation prévue](docs/INSTALLATION.md)

## Patch de test

Le projet propose désormais une [construction automatisée de l'archive Unreal V11](../../actions/workflows/build-test-pak.yml) via GitHub Actions. La procédure doit :

1. Décoder le `Game.locres` français précompilé ;
2. Vérifier son empreinte SHA-256 ;
3. Fabriquer un `NuclearNightmare-FR_P.pak` indépendant ;
4. Réouvrir l'archive et comparer les données extraites avec le `Game.locres` attendu ;
5. Fournir un ZIP **TEST**, non une Release publique.

**Important :** le fonctionnement réel en jeu n'est pas confirmé. Ce prototype remplace les ressources de la langue **russe** ; si le jeu charge bien le mod, il faudra sélectionner **Russe** dans les paramètres. C'est une solution provisoire pour ne pas modifier les fichiers du jeu ni son menu de langues.

Le patch final recherché sera un simple `.pak` à copier, sans installateur et sans EXE.

## Crédit

Projet de traduction : **FantinHD**.

- [YouTube](https://www.youtube.com/@TheFirstDog)
- [Google Play](https://play.google.com/store/apps/dev?id=8088754359282570640)

*Traduction fan non officielle. Les droits sur le jeu et ses ressources appartiennent à leurs ayants droit. Une copie légitime du jeu est nécessaire.*
