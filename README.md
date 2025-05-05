



##  Objectif

Appliquer plusieurs modèles de classification pour prédire une variable cible binaire à partir de données médicales anonymisées.

### Caractéristiques disponibles

##  Variables explicatives

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



## Organisation du dépôt

```
├── data/                       # Jeux de données bruts et prétraités
│   └── smoking.csv             #  dataset principal
│
├── notebooks/                  # Jupyter pour exploration et modélisation
│   ├── 01_exploration.ipynb    # Analyse descriptive et nettoyage
│   ├── 02_models.ipynb         # modeles lineaires, non lineaires et autres.. mais aussi l'optimisation et tuning 
│   └── 03_interpretation.ipynb # Explicabilité 
│
├                               
│   ├── models.py               # Modules Python avec des fonctions réutilisables
│
├── requirements.txt            # Package Python
├── README.md                   # Présentation rapide du projet
└── 
└── tabac.md                     # Résultats et commentaires du projet 
```



## Utilisation

- **Exploration des données** :  Pour explorer les données et les comprendre `notebooks/01_exploration.ipynb`
- **Modèles de base** : Nous permet de tester plusieurs modeles  `notebooks/02_models.ipynb`
- **Optimisation** : configurer et optimiser dans `notebooks/03_optimisation.ipynb` 
- **Explicabilité** : interpréter modèles et prédictions avec `notebooks/04_interpretation.ipynb`



---

*Dernière mise à jour : avril 2025*

