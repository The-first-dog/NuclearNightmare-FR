# Avancement de la localisation française

**19 octobre 2026 — version de travail**

- **1 463 / 1 463** identifiants disposent d'une proposition en français.
- **1 454** brouillons à relire.
- **9** entrées demandant une vérification prioritaire dans le jeu (rapports longs, chaînes de test et confirmations).
- **0** différence détectée sur les paramètres du type `{0}`, `{username}`, `%s`.
- Reconstruction d'un `Game.locres` version 3 réussie localement à partir des fichiers anglais/russe de référence.
- **Aucun mod `.pak` compatible testé ni publié.**

## Limitations actuelles

Le jeu comprend 781 entrées dans `en/Game.locres` et 1 407 dans `ru/Game.locres` ; l'union donne 1 463 clés. **92 clés communes ont des hashes source différents** et devront être contrôlées en jeu. Certaines chaînes proviennent uniquement de la localisation russe ; une relecture contextuelle est importante.

La couverture de 100 % signifie que chaque clé a une proposition, **pas que la qualité linguistique et le chargement en jeu sont validés**.

## Prochaines tâches

1. Relecture et cohérence terminologique : documents confidentiels, équipements, créatures, lieux.
2. Vérification des neuf chaînes sensibles et des longues notes.
3. Validation des retours à la ligne et de la largeur des composants d'interface.
4. Essai du chargement de `fr/Game.locres` ou de la substitution de langue sur une copie légitime.
5. Construction d'un `.pak` autonome avec un nom et un ordre de chargement compatibles.
6. Test sur une version déterminée du jeu, puis publication d'une Release ZIP avec SHA-256.

## Mise à jour des textes

Le CSV du dossier `translations/` est la source de référence. Ne pas modifier les clés Unreal (`Cle`, `Namespace`) et les hashes. Toutes les suggestions sont provisoires et ne constituent pas encore une version finale.
