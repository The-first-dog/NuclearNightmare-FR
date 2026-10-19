# État technique — Nuclear Nightmare FR

**Dernier point : 19 octobre 2026**

## Couverture des textes

- **1 463 / 1 463** identifiants de localisation ont une proposition française.
- Le fichier anglais fournit **781** entrées, le russe **1 407** ; **725** sont partagées.
- **11** traductions alternatives ont été retenues lorsque le texte russe différait de l'anglais.
- **92** entrées anglaises/russes portent des hashes de source différents.
- Tous les textes français sont renseignés et tous les identifiants sont uniques.

**Attention :** la couverture de 100 % ne signifie pas que 100 % des formulations sont vérifiées en contexte. Il reste des brouillons et des textes à raccourcir ou corriger selon les retours des joueurs.

## Validation de la structure

- Le `Game.locres` français version 3 a été reconstruit à partir des ressources localisées du jeu.
- Le fichier construit contient les **1 463** entrées attendues.
- Le `.pak` version 11 comporte seulement `NuclearNightmare/Content/Localization/Game/ru/Game.locres`.
- Le ZIP d'installation contient seulement `NuclearNightmare/Content/Paks/NuclearNightmare-FR_P.pak`.
- Le constructeur local a vérifié les tailles, empreintes et pointeurs internes. La GitHub Action effectue une vérification supplémentaire avec `repak` avant la mise en ligne.

## Compatibilité

- L'utilisateur indique avoir pu tester favorablement le système de traduction via l'emplacement russe.
- La version Linux/Proton du jeu ne fonctionne pas sur son poste, et **la compatibilité Linux n'est pas attestée**.
- La candidate `v1.0.0-rc.1` est destinée à être testée sur une copie originale du jeu avant toute qualification de version stable.

## Distribution

La procédure publie une **Release candidate** depuis GitHub Actions lorsque l'archive a été reconstruite et relue avec `repak`. La visibilité publique du dépôt doit être activée par son propriétaire dans les réglages GitHub.

La publication ne concerne **pas** le Steam Workshop : le patch GitHub est une installation manuelle pour les propriétaires du jeu sur Steam.
