# Plan de test du patch français

**Version candidate :** `v0.1.0-test`  
**État :** archive technique construite ; exécution de Nuclear Nightmare non encore validée.  
**Langue détournée :** russe (`ru/Game.locres`). Le sélecteur affichera donc « Russe » pendant ce premier test.

## Installation

1. Ouvrir Steam → Bibliothèque → Nuclear Nightmare → Propriétés → Fichiers installés → Parcourir.
2. Fermer le jeu.
3. Décompresser `NuclearNightmare-FR-TEST.zip`.
4. Fusionner le dossier `NuclearNightmare` du ZIP avec celui du jeu.
5. Vérifier l'ajout de `NuclearNightmare/Content/Paks/NuclearNightmare-FR_P.pak`.
6. Ne pas remplacer `NuclearNightmare-Windows.pak`.
7. Relancer le jeu, sélectionner « Russe » dans les paramètres.

## Vérifications en jeu

- [ ] Le jeu démarre normalement sans plantage.
- [ ] En sélectionnant « Russe », les menus apparaissent en français.
- [ ] Les boutons permettent toujours la navigation et la confirmation.
- [ ] Les paramètres, les descriptions et les objectifs s'affichent correctement.
- [ ] Les caractères français (é, è, à, ç, œ) sont visibles.
- [ ] Les traductions ne dépassent pas des encadrés et n'écrasent pas les contrôles.
- [ ] Une partie peut être démarrée et poursuivie.
- [ ] Les messages en cours de partie, documents et objets sont traduits.
- [ ] Retour à la langue anglaise possible.
- [ ] En supprimant le seul fichier `NuclearNightmare-FR_P.pak`, le jeu revient à l'état initial.

## En cas d'erreur

Ouvrir une Issue GitHub avec : capture d'écran, description, version du jeu (et idéalement date du build), système (Windows ou Proton/Bazzite), moment où le problème survient et étapes pour reproduire.

## Vérifications automatiques déjà réalisées localement

- LocRes v3 reconstruit depuis les ressources de localisation d'une copie du jeu.
- 1 463 identifiants conservés, avec zéro traduction vide.
- 11 variantes françaises spécifiques à des chaînes russes divergentes.
- Archive `.pak` V11 créée, index et empreintes vérifiés par le constructeur.
- ZIP contenant uniquement `NuclearNightmare/Content/Paks/NuclearNightmare-FR_P.pak`.

**Limite essentielle :** ces validations de structure ne remplacent pas un test avec le jeu. La construction GitHub Actions doit encore confirmer l'interopérabilité du PAK via repak.
