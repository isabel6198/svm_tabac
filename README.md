
## Nom du projet :

**Prédiction du statut tabagique à partir de données biologiques issues d’examens de santé en Corée du Sud (2002–2015)**

Réalisé dans le cadre du Master 2 Économétrie et Statistiques Appliquées de l'IAE de Nantes, par :

- LABRE-BLANC Emma

- PALACIO Gloria Isabel


##   Objectif:

Appliquer plusieurs modèles de classification afin de prédire le statut tabagique (fumeur ou non) à partir de données médicales anonymisées issues d’examens de santé


##  Reproductibilité du projet

- Le projet a été développé avec **Python 3.9.6**.  
- Les bibliothèques nécessaires sont listées dans le fichier **requirements.txt** pour faciliter l’installation de l’environnement.  
- Le projet est structuré en **notebooks** pour suivre les différentes étapes :

  - 01_exploration.ipynb : chargement des données, nettoyage et visualisation initiale  
  - 02_models.ipynb : entraînement, comparaison et optimisation des modèles  
  - 03_interpretation.ipynb : analyse de l’importance des variables et interprétation des prédictions (PDP, LIME, SHAP, etc.)

- Fichier utils.py

Ce fichier contient plusieurs **fonctions utilitaires** utilisées tout au long du projet, notamment pour la **préparation des données** et **l’explicabilité des modèles** :


- winsorize_data(xtrain, xtest, feature)

  Applique une **winsorisation** à une variable continue pour limiter l’impact des valeurs extrêmes

- detect_variable_types(df)

  Analyse automatiquement un DataFrame et retourne les variables **numériques**, **catégorielles**, **booléennes** ou **dates**.  

- display_original_pdp_values(num_col, model, df, scaler, feature_names)

  Permet de **représenter les PDP** avec les **valeurs non standardisées**, en inversant la transformation du StandardScaler 




## Organisation du dépôt

```
├── data/                                         #  Jeux de données bruts et prétraités
│   └── smoking.csv                               #  dataset principal
│   └── df_clean.csv                              #  dataset avec les variables choisies pour modelisation
│
├── image/                                        #  images
│
├── notebooks/                  
│   ├── 01_exploration.ipynb                      # Analyse descriptive et nettoyage
│   ├── 02_models.ipynb                           # modelisation et optimisation
│   └── 03_interpretation.ipynb                   # Explicabilité 
│
├── utils.py                                      # Fonctions 
│
├── .gitignore                                    # fichiers à ignorer 
├                           
├── requirements.txt                              # Packages necessaires Python
│                       
├── README.md                                     # Présentation rapide du projet
│                              
└── Projet_SVM_PALACIO_LABRE-BLANC_M2ECAP.md      # Résultats et commentaires du projet 

```




## Données & Variables:

###  Variables explicatives

- **Audition (oreille gauche / droite)** : 1 = normale, 2 = anormale
- **Colonne "oral"** : acceptation de l'examen oral (toutes les valeurs sont `True`, colonne à supprimer)
- **Poids** : par tranche de 5kg
- **Taille** : par tranche de 5cm
- **Acuité visuelle (œil gauche / œil droit)** : entre 0.1 (bonne vue) et 9.9 (cécité)
- **Tranche d’âge** : de 5 à 85+ (classe d’âge)
- **Sexe** : F ou M
- **Tour de taille (Waist)** : en cm
- **Pression artérielle systolique (BP_HIGH)** : mmHg
- **Pression artérielle diastolique (BP_LWST)** : mmHg
- **Glycémie à jeun (BLDS)** : mg/dL
- **Cholestérol total (TOT_CHOLE)** : mg/dL (150-250 mg/dL est la norme)
- **Triglycérides (TRIGLYCERIDE)** : mg/dL (norme entre 30 et 135 mg/dL)
- **HDL Cholestérol (HDL_CHOLE)** : mg/dL (30-65 mg/dL recommandé)
- **LDL Cholestérol** : mg/dL (au-dessus de 170 = hyperlipidémie)
- **Pigments sanguins (HMG)** : hémoglobine, g/dL
- **Protéines dans les urines (OLIG_PROTE_CD)** :
  - 1 = (-) Normal
  - 2 = (±) Trace
  - 3 = (+1) Faible
  - 4 = (+2) Modérée
  - 5 = (+3) Importante
  - 6 = (+4) Sévère
- **Créatinine** : mg/dL (norme 0.8~1.7 mg/dL)
- **AST** : UI/L (fonction hépatique, norme 0–40)
- **ALT** : UI/L (enzyme hépatique, norme 0–40)
- **GTP** : UI/L (enzyme hépatique)
  - Homme : 11–63 UI/L
  - Femme : 8–35 UI/L
- **Caries dentaires (dental carie)** : 0 = aucune, 1 = oui
- **Tartre (tartar)** : 0 = aucun, 1 = présent


### Variable cible

- **Tabagisme (smoking)** : 1 = ne fume pas, 2 = fume



---

*Dernière mise à jour : avril 2025*

