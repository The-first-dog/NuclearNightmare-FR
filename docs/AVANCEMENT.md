# Avancement — 19 octobre 2026

## Localisation

- **1 463 / 1 463** entrées ont un brouillon français.
- **1 443** entrées n'ont pas encore fait l'objet d'une vérification ciblée.
- **11** textes ont été révisés manuellement ; ils restent à tester en contexte.
- **9** textes sensibles (rapports narratifs, instructions longues et textes de test) restent à vérifier prioritairement en jeu.
- **11** variantes françaises spécifiques aux chaînes russes ont été ajoutées pour corriger de véritables divergences anglais/russe.
- **92** clés ont un hash de source différent entre les deux localisations.
- Les balises de formatage et variables ont été contrôlées par le script ; les **1 463** entrées ont passé la reconstruction en `.locres` v3.

## Patch technique

- Archive du jeu d'origine : Unreal Engine PAK V11, mount point `../../../`, seed `0x42459304` (1111855876).
- Cible provisoire : `NuclearNightmare/Content/Localization/Game/ru/Game.locres`.
- Constructeur local : `tools/construire_pak_test.sh` (nécessite le programme `repak` installé et les archives sources de sa copie du jeu).
- Un workflow GitHub Actions produit un ZIP de test et vérifie les octets du `.locres` à l'intérieur du `.pak` construit.

**Le chargement effectif du mod dans le jeu n'a pas été vérifié.** Une vérification statique du conteneur n'est pas un test d'intégration Unreal.

## Prochain contrôle

1. Vérifier que le workflow a abouti et que le ZIP est bien téléchargé depuis ses artefacts.
2. Copier le `.pak` de test dans `NuclearNightmare/Content/Paks/` sans remplacer l'archive du jeu.
3. Passer la langue sur **Russe** et vérifier menus, objectifs, descriptions et rapports.
4. Vérifier les effets d'un patch sur un jeu mis à jour, les textes non couverts par `.locres`, et la présence des glyphes français.
5. Corriger d'éventuelles erreurs, puis publier une Release lorsque les tests sont réussis.

**Ne pas présenter ce travail comme une traduction intégralement relue.**
