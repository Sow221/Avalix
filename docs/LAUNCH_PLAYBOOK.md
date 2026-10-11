# Playbook de lancement open source + LinkedIn (projet personnel)

> Statut des sources : le web ne donne que des blogs marketing/recrutement, pas de données
> officielles LinkedIn ni de statistiques de recruteurs. Les chiffres cités sont des **ordres
> de grandeur contestables** ; les principes (preuve > adjectifs, dwell time, README clair) sont
> en revanche cohérents entre sources. Sources en bas de page.

## 1. Positionnement (à décider avant tout)

Ce n'est pas un projet de fin de cycle : c'est une **implémentation de référence personnelle**.
Une phrase à fixer partout (README, bio GitHub, post, CV) :

> « Plateforme de scoring de crédit de bout en bout (features, anti-fuite, modèle calibré, API,
> monitoring de dérive, IaC), validée sur Lending Club ; prête à ingérer des données réelles. »

Public cible, par ordre : (1) recruteurs / hiring managers ML-Data, (2) pairs ingénieurs
MLOps/credit risk, (3) fintech/SFD UEMOA. Un seul message principal par canal.

## 2. Ce que les profils « top » ont en commun

| Critère | Ce que les meilleurs montrent | État du dépôt |
|---|---|---|
| Profondeur > quantité | 1-2 projets complets plutôt que 5 notebooks | OK |
| Propriété de bout en bout | données → modèle → API → déploiement → monitoring | OK |
| Preuves reproductibles | `make` en une commande, lockfiles, CI verte | OK (vérifier le quickstart à froid) |
| Rigueur d'évaluation | split temporel, calibration, ablation, robustesse, équité | OK |
| Honnêteté des limites | « données synthétiques », model card, ADR | OK, à garder |
| Résultat chiffré cadré métier | coût / latence / alertes détectées, pas juste l'AUC | À mettre en avant |
| Démo accessible en 30 s | URL cliquable, GIF, captures | Partiel (Render s'endort) |
| Signal communautaire | issues « good first issue », releases, changelog | À faire |

## 3. Livrables à produire avant de poster (ordre de priorité)

1. **README « 30 secondes »** : une phrase, un GIF/capture de la démo Swagger, un schéma
   d'architecture, 3 chiffres vérifiables, un quickstart de 3 commandes. Tout le reste dans
   `<details>` ou `docs/`.
2. **Release GitHub `v1.2.x`** avec notes (extrait du CHANGELOG) + tag. Une release est un
   objet partageable et horodaté.
3. **Schéma d'architecture** (Excalidraw / Figma / draw.io) en PNG + SVG, fond neutre.
4. **Graphique signature** : le rejeu de monitoring (PSI sur 24 mois, 4 alertes) est la pièce la
   plus originale. En faire un visuel propre, annoté, lisible sur mobile.
5. **Démo toujours up** (ou GIF enregistré si l'hébergement gratuit s'endort).
6. **Fichiers communautaires** : `SECURITY.md`, `CODE_OF_CONDUCT.md`, templates d'issue/PR,
   3-5 issues `good first issue`, topics GitHub, image sociale (1280×640) du dépôt.
7. **Post LinkedIn réécrit** (les chiffres de `docs/LINKEDIN_POST.md` sont obsolètes).
8. Optionnel : article long (dev.to / Medium / LinkedIn) « ce que 24 mois de rejeu de
   monitoring m'ont appris », pour le référencement et pour alimenter les posts suivants.

## 4. Stratégie de post LinkedIn

### Format
- **Carrousel PDF (6-10 slides, 1 idée par slide)** : format le plus cité pour le temps passé
  (dwell time) et les sauvegardes. À privilégier pour le lancement.
- Alternative : image unique (graphique signature) + texte court.
- **Lien GitHub dans le premier commentaire ou en bio** plutôt que dans le corps : les sources
  convergent sur une pénalité des liens sortants (ampleur incertaine, 19 % à ~60 % selon les
  blogs). Ne pas compter sur l'astuce du « lien en commentaire » comme garantie : certains
  affirment qu'elle est détectée. Test A/B personnel conseillé.

### Structure du carrousel
1. Accroche : problème + résultat (« 24 mois rejoués : 4 alertes de dérive réelles »).
2. Le problème (décision de crédit en UEMOA, grilles manuelles, pas de suivi).
3. Architecture (le schéma).
4. Ce qui est rigoureux (split temporel, anti-fuite, calibration).
5. La preuve (graphique de monitoring).
6. Ce qui est honnête (synthétique + Lending Club, pas de données CIF réelles).
7. Ce que j'ai appris / décisions difficiles.
8. Comment contribuer + lien (« repo en commentaire »).

### Texte d'accompagnement
- 1re ligne = promesse (visible avant « voir plus »). Pas d'emoji en rafale.
- 120-250 mots, phrases courtes, une seule question ouverte à la fin pour déclencher des
  commentaires de fond (« Vous monitorez la dérive en PSI ou en KS ? »).
- 3-5 hashtags max, pertinents.

### Calendrier
- **J-7 à J-1** : préparer visuels, README, release ; relire à froid ; tester le quickstart sur
  une machine propre.
- **J0 (mardi-jeudi, matin heure locale)** : publier ; rester disponible 60-90 min pour
  répondre vite (les blogs s'accordent sur l'importance de la première heure).
- **J+1 à J+14** : 3-4 posts de suite, un angle chacun (monitoring, anti-fuite, calibration,
  IaC). Le lancement n'est qu'un épisode d'une série.
- Mesurer : impressions, saves, étoiles GitHub, clones, issues ouvertes.

### Où d'autre poster
GitHub (release + topics), r/MachineLearning / r/mlops (selon les règles de chaque forum),
Hacker News « Show HN » (si démo stable), dev.to, communautés Africa AI / data. Adapter le
texte à chaque canal, ne pas copier-coller.

## 5. Visuels et outils

- Palette sobre (2 couleurs + neutre), une police unique, contraste élevé, lisible sur mobile.
- Un graphique = un message ; titre qui énonce la conclusion, pas le sujet.
- Outils : Figma / Canva (carrousels), Excalidraw (schémas), matplotlib/plotly exportés en SVG
  puis PNG 2x (graphiques), enregistrement d'écran → GIF < 10 Mo (démo).
- Une image sociale du dépôt (1280×640) pour que le lien partagé ait un bel aperçu.

## 6. Pièges à éviter

- Annoncer « Production » alors que c'est une implémentation de référence sur données non CIF.
- Chiffres divergents entre README, post et model card (cohérence = crédibilité).
- Utiliser le nom « CIF » comme s'il s'agissait d'un produit officiel sans accord explicite.
- Poster sans démo cliquable, ou avec une démo qui met 60 s à se réveiller.
- Acheter de l'engagement, ou demander des étoiles en masse : contre-productif.

## 7. Check-list J0

- [ ] Quickstart testé sur machine propre
- [ ] CI verte sur `main`, release taguée
- [ ] README retravaillé (GIF, schéma, 3 chiffres cohérents)
- [ ] Mention de non-affiliation + accord sur le nom si besoin
- [ ] Scan de secrets sur tout l'historique
- [ ] SECURITY.md, CODE_OF_CONDUCT.md, templates, issues `good first issue`
- [ ] Carrousel PDF exporté, lisible sur mobile
- [ ] Texte du post relu, lien prêt pour le 1er commentaire
- [ ] Plan de réponse pendant 90 min après publication

## Sources

- [LinkedIn Algorithm 2026 : Documents, Newsletters, Video (Dataslayer)](https://www.dataslayer.ai/blog/linkedin-algorithm-february-2026-whats-working-now)
- [LinkedIn Carousel vs Text Post 2026 (GrowLeads)](https://growleads.io/blog/linkedin-carousel-vs-text-post-2026/)
- [LinkedIn organic in 2026 (Perroly)](https://www.perroly.com/blog/linkedin-organic-2026-what-works)
- [LinkedIn Algorithm 2026 (SocialPilot)](https://www.socialpilot.co/blog/linkedin-algorithm)
- [The ML portfolio that actually gets you hired in 2026](https://letsdatascience.com/blog/the-ml-portfolio-that-actually-gets-you-hired-in-2026)
- [Machine Learning Engineer Portfolio (Interview Kickstart)](https://interviewkickstart.com/blogs/articles/machine-learning-engineer-portfolio)
- [Data engineering projects hiring managers want (Data Engineer Academy)](https://dataengineeracademy.com/blog/portfolio-to-paycheck-7-data-engineering-projects-hiring-managers-actually-want-in-2025/)
- [How to write a great README (thoughtbot)](https://thoughtbot.com/blog/how-to-write-a-great-readme.md)
- [README Basics (JHU OSPO)](https://ospo.library.jhu.edu/wp-content/uploads/sites/60/2024/07/OSPO-Explainer_-README-Basics-Slides.pdf)
