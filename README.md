# Yes-Pro – Pipeline open‑source pour la personnalisation des thérapies sonores

Ce projet est un **pipeline méthodologique réutilisable** qui montre comment enchaîner acquisition EEG, prétraitements, fusion de données cliniques et apprentissage automatique pour estimer la réponse à différentes thérapies acoustiques chez des patients acouphéniques. Avec le petit échantillon actuellement disponible (89 patients), les performances restent modestes ; le code est donc fourni avant tout comme **base de travail à enrichir** avec des données supplémentaires et des variantes d’algorithmes.

## Contexte et objectif

Les acouphènes chroniques affectent près de 10 % de la population adulte. La médecine s’appuie encore largement sur des essais/erreurs pour sélectionner une thérapie sonore, faute de biomarqueurs robustes. Yes‑Pro vise à illustrer un flux de travail reproductible qui pourrait, à terme, recommander la thérapie la plus appropriée une fois que des bases de données plus riches auront été constituées.

## Jeu de données actuel

* Source : « Acoustic Therapies for Tinnitus Treatment: An EEG Database » (Mendeley Data, 2022).
* 89 patients et 14 témoins, suivis pendant huit semaines.
* Cinq protocoles : musique relaxante (placebo), TRT, TEAE, TBB, ADT.
* Variables : 95 descripteurs EEG + méta‑données cliniques (âge, sexe, scores THI/HADS).
* Cible : variation du score THI entre la première et la huitième semaine.

> Ce volume de données est insuffisant pour entraîner des modèles généralisables ; les résultats doivent être interprétés comme des ordres de grandeur plutôt que comme des seuils de décision.

## Pipeline proposé

1. Prétraitement EEG : filtrage 1–45 Hz, notch 50 Hz, référenciation moyenne, fenêtres de 2 s avec recouvrement de 50 %.
2. Extraction de caractéristiques : densités spectrales de puissance par bande (delta → gamma) et asymétries hémisphériques.
3. Fusion des caractéristiques EEG et cliniques dans une matrice unique.
4. Banc d’essai d’algorithmes supervisés : k‑NN, Voting Regressor, Ridge/Lasso, SVR, LightGBM, Random Forest, XGBoost, MLP.
5. Évaluation : division 80/20, MSE et R², interprétation SHAP.

Chaque bloc est encapsulé dans des fonctions Python indépendantes, afin de faciliter le remplacement d’étapes (p. ex. filtrage, modèles).

## Résultats de référence (baseline)

| Modèle  | MSE   | R²    |
| ------- | ----- | ----- |
| k‑NN    | 9.73  | 0.17  |
| Voting  | 10.48 | 0.11  |
| Ridge   | 11.61 | 0.01  |
| XGBoost | 33.16 | –2.46 |

Les scores négatifs ou proches de zéro soulignent la **sous‑adaptation** liée au manque de données. Ces chiffres constituent une ligne de base à améliorer.

## Comment réutiliser le pipeline

1. Lancer les différents notebook : process.ipynb > ia.ipynb pour générer de nouveaux modèles de référence.
2. Explorer les interprétations SHAP pour guider la sélection de biomarqueurs.
3. Contribuer via pull‑requests pour mutualiser améliorations et jeux de données.

## Forces et limites

| Forces                                       | Limites                                     |
| -------------------------------------------- | ------------------------------------------- |
| Pipeline complet, versionné et reproductible | Cohorte restreinte et hétérogène            |
| Modulaire : chaque étape peut être remplacée | Données manquantes pour quelques variables  |
| Interprétation SHAP incluse                  | Performances insuffisantes pour la clinique |

## Perspectives

* Constituer des bases de données multicentriques pour passer le cap des centaines de patients.

* Tester d’autres biomarqueurs (IRM fonctionnelle, HRV).

* Valider le tout au cours d’un essai contrôlé randomisé.

## Équipe&#x20;

Betry S., Boulac I., Calujek C., Cazier G., Dufour H., Langrand M., Thuillier L.
Formation Big Data, IA & E‑Santé – JUNIA (Promo 66, 2024‑2025).
