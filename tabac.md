# Données :

échantillon issu des données de ce site : 데이터 상세 | 공공데이터포털

Les données ouvertes nationales sont des données publiques détenues par le Service national d'assurance maladie conformément au cadre politique du Gouvernement coréen.  
Les données ouvertes sont les données accumulées par les membres de l'assurance maladie nationale, la KHIC remplissant son rôle de fournisseur d'assurance maladie nationale.  
Les données ouvertes comprennent notamment les informations relatives à l'historique des traitements médicaux, les informations relatives aux prescriptions de médicaments et les informations relatives aux examens médicaux.  
Afin d'ouvrir les données en toute sécurité les informations personnelles et les données sensibles sont exclues ou masquées et ouvertes par des experts externes.  
Les données fournies vont de 2002 à 2015.

Les infos personnelles permettant d’identifier une personne (numéro de sécurité sociale, numéro d’assurance maladie, nom…) ont été exclues. ou dépersonnalisée avec des techniques comme la catégorisation des groupes d’âge…

Les données sont des infos sur l’historique des traitements médicaux, des prescriptions et des résultats des examens de santé d’un million de membres de l’assurance nationale entre 2002 et 2015.  
La sélection d’un million de personne a été effectuée à l’aide d’une technique de sélection aléatoire et cette base de données contient des informations relatives aux examens de santé tirées de l’ensemble de données nationales de corée sur la santé.

Nous analysons un échantillon de cette base de données trouvé sur Kaggle et permettant une classification binaire

# Variables explicatives :

- Pour l’audition, 1 signifie une audition normale et 2 signifie une audition anormale.

- Pour la colonne orale, il s’agit de savoir si le candidat a accepté l’examen oral. (Toutes les observations sont vraies. Par conséquent, ils peuvent être supprimés)

- poids (par tranche de 5kg) et taille (hauteur par tranche de 5cm)

- accuité visuelle de l'oeil gauche et de l'oeil droit exprimé par une valeur comprise entre 0,1 et 2,5 où 0,1 correspond à l'accuité visuelle et 9,9 à la cécité

- audition de l'oreille gauche et droite : 1 normal, 2 anormal

- Afin de dépersonnaiser des tehniques ont été appliquée comme faire des classes d'âge : age in range 5 et à partir de 85+ dans la catégorie 85+

- gender : F ou M

- Waist : tour de taille en cm

- pression arterielle systolique (BP_HIGH) : Le cœur se contracte avec une grande force à la pression artérielle la plus élevée de l'examinateur.  
  La pression intravasculaire lorsque le cœur se contracte et pousse le sang dans les artères. (mmHg)
- pression arterielle diastolique (BP_LWST) : la pression artérielle du coeur en diastole comme la pression artérielle la plus basse (mmHg)

- glycémie préprandiale (glycémie à jeun) (BLDS) : Glycémie préprandiale du testé (concentration de glucose dans 100 ml de sang) (mg/dL)

- Cholesterol total (TOT_CHOLE) : Somme du cholestérol estérifié et du cholestérol non estérifié (libre) dans le sérum.  
  La normale est de 150-250 mg/dL Le cholestérol non estérifié (libre) représente environ un tiers et le reste est constitué d'esters de cholestérol.

- Triglycérides (TRIGLYCERIDE) : Lipides simples ou neutres. L'estérification du glycérol avec trois molécules d'acides gras et sont les dérivés lipidiques les plus courants dans la nature. (normale entre 30 et 135 mg/dL) (mg/dL)

- HDL Cholesterol (HDL_CHOLE) : Cholestérol dans les HDL (lipoprotéines de haute densité) petites particules de cholestérol qui sont attirées par les cellules et renvoyées vers le foie et aide à éliminer l'accumulation de mauvais cholestérol sur les parois des vaisseaux sanguins. Le taux normal se situe entre 30 et 65 mg/dL.

- cholesterol dans les LDL (lipoprotéines de basse densité) :  Cholestérol dans les LDL (lipoprotéines de basse densité) Lorsque la quantité de cholestérol à très grosses particules augmente excessivement, il s'accumule dans les parois des vaisseaux sanguins, provoquant l'athérosclérose et diverses maladies. Des taux supérieurs à 170 mg/dL sont généralement considérés comme une hyperlipidémie. (mg/dL)

- Pigments sanguins (HMG) : protéine pigmentée présente dans le sang ou les cellules sanguines, composées de globine et d'hème, qui joue le rôle de transporteur d'oxygène dans le sang (g/dL)

- Protéines (OLIG_PR OTE_CD) : protéines dans les urines noté comme 1 (-), 2(+-), 3 (+1), 4(+2), 5(+3), 6(+4)  
  Code	Interprétation	Signification médicale approximative  
  1	(-)	Absence de protéines (normal)  
  2	(±)	Trace (limite basse, douteuse)  
  3	(+1)	Faible présence de protéines  
  4	(+2)	Protéinurie modérée  
  5	(+3)	Protéinurie importante  
  6	(+4)	Protéinurie sévère  

- Créatinine (creatinine) : La créatinine est un déshydraté de la créatine, un produit final du métabolisme des protéines endogènes, excrété par les reins. Elle est excrétée par les reins et son augmentation est liée au développement musculaire et à l'exercice, indépendamment de l'alimentation.  
  Les concentrations de créatinine sérique augmentent en cas de dysfonctionnement rénal. Valeur normale 0,8~1,7mg/dL

- smoking : si la personne fume : 1 ne fume pas, 2 fume

- AST : Valeurs des tests sanguins indiquant la fonction hépatique et, outre les cellules du foie, le cœur et les reins,  
  le cœur, les reins, le cerveau, les muscles, etc. La concentration augmente lorsque ces cellules sont endommagées. Normal 0 à 40 UI/L

- ALT : L'ALT est une enzyme qui se trouve principalement dans les cellules du foie et dont la concentration augmente lorsque les cellules du foie sont endommagées. Normal 0 à 40 UI/L

- GTP : Valeur d'un test sanguin indiquant la fonction hépatique. Enzyme présente dans les canaux biliaires du foie, qui transforme l'acide glutamique en peptides et en acides aminés, Elle augmente dans le sang lorsque l'excrétion de la bile dans la vésicule biliaire est déficiente et que des troubles des cellules hépatiques se produisent. Valeur normale 11~63UI/L chez l'homme, 8~35UI/L chez la femme.

- dental carie : présence ou l'absence de caries dentaires pour cet examiné 0 (aucune), 1 (oui)

- tartar : Si le candidat a du tartre 0 (aucun), 1 (présent)




# ----------------------

# I.EDA

### Téléchargement

Le jeu de données a été téléchargé et copié dans le dossier `./data` du projet.  
Après chargement dans un DataFrame pandas, celui-ci contient **55 692 observations** et **27 variables**.  
Aucune valeur manquante n’a été détectée dans l’ensemble des colonnes. 


Bien que `df.duplicated().sum()` indique 0 doublon, en excluant la colonne `ID` (identifiant unique), nous avons détecté **11 140 doublons** sur les autres colonnes.  
Cela signifie que plusieurs individus possèdent des enregistrements strictement identiques, à l’exception de leur identifiant.  
Ces doublons ont été supprimés pour éviter de biaiser l’analyse.



# ---------------------------------------------------------------
### Nettoyage des types de variables

Avant toute analyse, les noms de colonnes ont été uniformisés en remplaçant les espaces par des underscores (`_`) pour faciliter la manipulation avec pandas.


### Recatégorisation des variables
Après détection  des types, certaines variables ont été reclassées  pour mieux refléter leur nature.
Les transformations suivantes ont été effectuées directement dans le DataFrame :

- Suppression des colonnes non informatives (`ID`, `oral`)
- Recodage de `gender` en variable binaire (`homme`), puis conversion en type `bool`
- Création de variables indicatrices pour les problèmes d'audition (`pb_hearing(left/right)`), converties en `bool`
- Recodage des colonnes booléennes (`tartar`, `dental_caries`, `smoking`) au format `bool`
- Suppression des colonnes d'origine devenues redondantes (`gender`, `hearing(...)`)
- Spécification de `Urine_protein` comme variable **catégorielle ordonnée** (de 1 à 6)

Enfin, une redétection propre des types (`numerical`, `categorical`, `boolean`) a été effectuée afin de structurer les prochaines étapes d’analyse exploratoire et de modélisation.




### Statistiques descriptives

Dans cette section, nous avons réalisé une analyse statistique descriptive de l’ensemble des variables du jeu de données. Cela nous a permis d’observer les tendances centrales, les éventuels déséquilibres ainsi que les valeurs extrêmes pouvant influencer l’analyse ou la modélisation.

---

#### 1. Variables numériques

On observe que :

- L’**âge moyen** des individus est de 44 ans, avec une population allant de 20 à 85 ans, ce qui reflète un échantillon adulte assez large
- Les **tailles** et **poids** moyens sont respectivement d’environ 165 cm et 66 kg
- Le **tour de taille** moyen est de 82 cm, ce qui pourra être utile dans l’évaluation des risques métaboliques
- L’**acuité visuelle** moyenne est autour de 1.0 pour chaque œil, mais on note des cas de déficience sévère (jusqu’à 9.9), indiquant potentiellement une cécité
- La **tension artérielle moyenne** est de 121.5 / 76 mmHg. Cependant, quelques valeurs minimales paraissent incohérentes (par exemple une systolique à 13 mmHg) 

---

#### 2. Variables biologiques (métaboliques)

Nous avons analysé les principaux marqueurs liés à la santé métabolique :

- La **glycémie à jeun** est en moyenne de 99 mg/dL, ce qui correspond à une population globalement saine, mais certaines valeurs très élevées (jusqu’à 505 mg/dL) nécessitent vigilance
- Le **cholestérol total** est en moyenne de 197 mg/dL, ce qui est dans la norme, mais on relève également des cas extrêmes
- Les **triglycérides** présentent une moyenne de 127 mg/dL, avec une distribution très asymétrique (jusqu’à 999 mg/dL)
- Le **HDL** (bon cholestérol) est globalement bon (57 mg/dL), mais on retrouve des valeurs incohérentes (jusqu’à 618 mg/dL)
- Le **LDL** (mauvais cholestérol) est en moyenne à 115 mg/dL, avec certaines valeurs aberrantes (jusqu’à 1860 mg/dL)

---

#### 3. Variables liées au sang, au foie et aux reins

Nous avons ensuite étudié des indicateurs plus cliniques :

- L’**hémoglobine** a une moyenne de 14.6 g/dL, mais on observe des extrêmes de 4.9 à 21.1 g/dL
- La **créatinine sérique**, indicateur de la fonction rénale, est en moyenne à 0.89 mg/dL. Une valeur très élevée à 11.6 mg/dL semble anormale
- Les **enzymes hépatiques** (AST, ALT, GTP) présentent des moyennes dans les normes (entre 26 et 40 UI/L), mais des pics très élevés (ex. : 2914 pour l’ALT) laissent supposer des erreurs ou cas cliniques extrêmes

---

#### 4. Variables catégorielles

On a exploré la répartition des modalités pour chaque variable catégorielle. Cela nous a permis d’observer :

- Des déséquilibres marqués, notamment pour `Urine_protein`, où plus de 94 % des individus sont au niveau `1.0`, indiquant l’absence de protéines dans les urines.
- Des valeurs rares, mais médicalement significatives, apparaissent dans les modalités supérieures (ex. `6.0` correspondant à une protéinurie sévère)

---

#### 5. Variables booléennes

Voici les principales observations :

- **21 %** des individus présentent des **caries dentaires**
- **37 %** sont **fumeurs**
- **64 %** sont des **hommes**, ce qui montre un certain déséquilibre dans la distribution par genre
- Les **problèmes d’audition** sont rares (≈ 2.6 % pour chaque oreille)
- **55 %** des individus présentent du **tartre dentaire**

Ces proportions confirment des déséquilibres de classe pour certaines variables, ce qui devra être pris en compte dans la modélisation.


Cette analyse descriptive nous a permis de mieux comprendre la structure et les caractéristiques de notre jeu de données.  
Elle révèle une population adulte majoritairement masculine, une proportion significative de fumeurs, et quelques variables présentant des valeurs extrêmes ou déséquilibrées.  



#####-----------------------------------------------------------------------à vérifier --------------------
### Comparaison des variables numériques selon le statut tabagique

Nous avons comparé les moyennes des variables numériques entre les individus fumeurs et non-fumeurs. Cette analyse met en évidence plusieurs différences significatives :

- Les **fumeurs sont plus jeunes**, mais présentent en moyenne un **poids**, un **tour de taille** et une **taille** supérieurs.
- Leur **tension artérielle** est légèrement plus élevée (systolique et diastolique).
- Ils ont une **glycémie à jeun plus élevée**, ce qui peut refléter un risque accru de troubles métaboliques.
- Leur **acuité visuelle** est légèrement meilleure en moyenne.
- Le **cholestérol total** est légèrement inférieur chez les fumeurs.

Ces écarts suggèrent que le statut tabagique est associé à des différences physiologiques notables, ce qui est cohérent avec les effets connus du tabac sur le métabolisme et la santé cardiovasculaire.
#####----------------------------------------------------------------------- --------------------

### Corrélations entre variables numériques

À partir de la matrice de corrélation de Spearman, nous avons identifié les relations les plus fortes entre variables numériques (ρ ≥ 0.7).  
Cela permet d’anticiper les redondances et d’orienter la sélection de variables.

Les principales corrélations observées sont :

- **`weight` et `waist(cm)`** : ρ = 0.81 — très forte corrélation entre poids et tour de taille
- **`eyesight(left)` et `eyesight(right)`** : ρ = 0.70 — corrélation logique entre les deux yeux
- **`systolic` et `relaxation`** : ρ = 0.74 — forte corrélation attendue entre les deux types de tension artérielle
- **`Cholesterol` et `LDL`** : ρ = 0.89 — corrélation très forte, le LDL étant une composante du cholestérol total
- **`AST` et `ALT`** : ρ = 0.73 — forte dépendance entre enzymes hépatiques


 **Corrélations linéaires (Pearson)**

Nous avons également examiné la matrice de corrélation de Pearson, qui évalue les relations linéaires entre les variables numériques. Les résultats confirment les principales dépendances identifiées précédemment avec Spearman :

- **Poids** et **tour de taille** : r = 0.82
- **Tension systolique** et **diastolique** : r = 0.76
- **LDL** et **cholestérol total** : r = 0.74
- **AST** et **ALT** (enzymes hépatiques) : r = 0.74
- **Taille** et **poids** : r = 0.68

Ces résultats nous aideront à détecter les variables redondantes et à  améliorer la parcimonie des modèles,

### Corrélation des variables numériques avec la cible `smoking`

Nous avons analysé la corrélation  entre chaque variable numérique et la cible `smoking`, dans le but d’identifier les variables les plus associées au statut tabagique.

Les variables les plus corrélées sont :

- `hemoglobin` (r ≈ 0.40) : les fumeurs ont en moyenne un taux d’hémoglobine plus élevé, ce qui reflète une adaptation physiologique à une oxygénation réduite
- `height`, `weight`, `waist` : les fumeurs sont légèrement plus grands et plus corpulents, ce qui pourrait refléter un biais lié au genre
- `triglyceride`, `HDL`, `Gtp` : plusieurs variables métaboliques et hépatiques présentent une corrélation modérée, suggérant un profil de santé différent chez les fumeurs

Les corrélations restent globalement faibles à modérées.


### Détection des outliers (méthode IQR)

Nous avons appliqué la méthode des interquartiles (IQR) pour identifier les valeurs aberrantes dans les variables numériques.  
Un point est considéré comme un outlier s’il se situe en dehors de l’intervalle `[Q1 - 1.5×IQR ; Q3 + 1.5×IQR]`.

Les variables avec le plus d’outliers sont :

- **GTP**, **ALT**, **AST** : marqueurs de la fonction hépatique avec de nombreuses valeurs extrêmes.
- **Créatinine**, **glycémie**, **triglycérides** : variables biologiques sensibles aux pathologies ou aux erreurs de saisie.
- **Acuité visuelle** et **HDL** : présentent aussi des écarts importants.


# Modélisation

Nous passons maintenant à la deuxième phase du projet : la modélisation.

Dans un nouveau notebook, nous commençons par préparer nos données en définissant :
- `X` : les variables explicatives (numériques, booléennes, et catégorielle ordonnée)
- `y` : la variable cible, ici `smoking` (binaire)

Nous effectuons ensuite une séparation entraînement/test classique pour évaluer nos modèles de manière robuste.


### Pipeline de prétraitement

Pour préparer les données à la modélisation, nous avons mis en place un pipeline de prétraitement  :

- Les **variables numériques** sont standardisées (`StandardScaler`) pour uniformiser les échelles
- La variable **`Urine_protein`**, considérée comme catégorielle ordonnée, est encodée via un `OrdinalEncoder`
- Les **variables booléennes** sont transmises telles quelles (`passthrough`), car elles sont déjà dans un format exploitable

Nous avons ensuite séparé les données d’entraînement et de test, puis appliqué le pipeline pour obtenir des données prêtes à l’emploi (`X_train_df`, `X_test_df`) en conservant les noms de colonnes associés.

### Évaluation comparative des modèles

### Modèles testés et justification

Nous avons entraîné et comparé plusieurs modèles de classification binaire pour prédire le statut tabagique (`smoking`), incluant :

- **Régression logistique**  
  Modèle **linéaire paramétrique**, simple et interprétable. Bien adapté comme **modèle de base** pour évaluer la linéarité des relations entre les variables et la cible.

- **Random Forest**  
  Modèle **non paramétrique** basé sur des arbres de décision, capable de **capturer des interactions non linéaires** et de **gérer les variables hétérogènes** (numériques, booléennes, ordinales). Il est également robuste aux outliers.

- **Gradient Boosting / XGBoost**  
  Modèles **non paramétriques puissants** qui construisent des arbres successifs pour corriger les erreurs précédentes. Bien adaptés aux **relations complexes**, aux **effets faibles** répartis sur de nombreuses variables, et souvent très performants avec un bon réglage.

- **SVM avec différents kernels (linéaire, RBF, polynomial)**  
  Les SVM sont des modèles **paramétriques flexibles** qui, via le `kernel`, permettent de projeter les données dans des espaces de dimension supérieure pour capter des frontières non linéaires.  
  Le **kernel linéaire** teste si une séparation linéaire est suffisante, tandis que les **kernels RBF** et **polynomial** permettent de modéliser des relations plus complexes.

- **Classifieurs linéaires : `LinearSVC` et `SGDClassifier`**  
  Modèles linéaires efficaces, particulièrement adaptés aux grands jeux de données.  
  `LinearSVC` repose sur une optimisation de la marge, tandis que `SGDClassifier` est une implémentation stochastique rapide, adaptée au traitement itératif.

---

Pour chaque modèle, nous avons mesuré :
- Les performances sur les jeux d'entraînement et de test (accuracy, précision, rappel, F1-score)

 | Modèle                | Recall    | F1-score  | Accuracy | Précision | Remarques clés                                 |
| --------------------- | --------- | --------- | -------- | --------- | ---------------------------------------------- |
| **Gradient Boosting** | **0.716** | **0.689** | 0.764    | 0.665     |  bon équilibre et rappel      |
| **LinearSVC**         | **0.721** | 0.682     | 0.754    | 0.647     | Meilleur rappel, modèle linéaire interprétable |
| SVC (Linear Kernel)   | 0.714     | 0.680     | 0.753    | 0.648     | Résultats proches de LinearSVC                 |
| Random Forest         | 0.693     | 0.677     | 0.758    | 0.663     | Performant mais moins bon rappel               |
| Logistic Regression   | 0.587     | 0.612     | 0.727    | 0.639     | Rappel insuffisant                             |
| SVC (RBF Kernel)      | 0.440     | 0.531     | 0.715    | 0.669     | Faible rappel, pas adapté ici                  |
| SVC (Poly Kernel)     | 0.475     | 0.563     | 0.730    | 0.691     | Bonne précision mais rappel trop faible        |
| SGDClassifier         | 0.012     | 0.024     | 0.637    | 0.784     | Échec complet sur le rappel                    |


- Les performances en validation croisée à 5 folds pour évaluer la stabilité des modèles

Et les résultats ont été résumés sous forme de tableau et visualisés pour faciliter la comparaison.

### Résultats comparés : 


#### Régression logistique
- Offre des performances stables (accuracy ≈ 71.7 %) sur les jeux d’entraînement et de test
- Modèle simple et interprétable, mais avec un **rappel limité (~54 %)**, ce qui signifie qu’il **rate beaucoup de fumeurs**

####  Random Forest
- Performances supérieures sur le jeu de test (accuracy ≈ 76.3 %, recall ≈ 70 %)
- Meilleur équilibre précision/rappel (F1-score ≈ 68.5 %)
- Toutefois, le modèle **overfit** complètement les données d'entraînement, atteignant **100 % de précision**, ce qui peut nuire à la généralisation





### ############### ============================= ###   ############### =============================
### ############### ============================= Mardi 6   ### ############### =============================

### Choix d’un modèle linéaire et non linéaire

Afin de disposer de deux approches complémentaires( un modèle performant, et un autre que l’on peut facilement interpréter), nous avons retenu un modèle linéaire et un modèle non linéaire parmi ceux testés.
Nous avons choisi ces deux modèles pour leur complémentarité :

Gradient Boosting pour sa puissance prédictive

LinearSVC pour sa capacité à expliquer les résultats











####  Modèle linéaire retenu : **LinearSVC**

- Il présente un **bon compromis entre performance et simplicité** :
  - Accuracy : 75.3 %
  - F1-score : 0.6823
  - Recall : 72.3 % 
- Il est **rapide à entraîner**, **interprétable** et compatible avec des techniques d’explicabilité  et interprétation

#### Modèle non linéaire retenu : **Gradient Boosting**
Paramètres utilisés par défaut 
learning_rate=0.1, n_estimators=100, max_depth=3
Ce sont les valeurs par défaut classiques, qui forment un modèle peu profond mais stable.
loss='log_loss'  configuration pour de la classification binaire (logistique)


- Il est **le plus performant globalement** :
  - F1-score test :
  - Recall : 
  - Moins sujet à l'overfitting que Random Forest ou XGBoost
- Il capture **des interactions complexes** entre les variables, ce qui le rend bien adapté à des données de santé hétérogènes
- Compatible avec des techniques d’explicabilité 



# Optimisation :

Traitement du déséquilibre de classes

Dans notre projet, nous cherchons à prédire si une personne est fumeuse ou non à partir de données. L’analyse descriptive révèle un déséquilibre modéré entre les classes : environ 63 % de non-fumeurs contre 37 % de fumeurs. Ce déséquilibre peut biaiser les modèles de classification, qui auront tendance à prédire majoritairement la classe majoritaire pour maximiser l'accuracy.

Or, Dans ce contexte, le coût d’un faux négatif (un fumeur non détecté) est plus élevé que celui d’un faux positif. Pour cette raison, la métrique de rappel (recall) a été privilégiée lors de l’évaluation des modèles.

Pourquoi utiliser le resampling ?
Pour corriger ce déséquilibre, nous avons envisagé deux approches :

Oversampling (RandomOverSampler) : consiste à dupliquer les exemples de la classe minoritaire (fumeurs).
(Inconvénient : risque de sur-apprentissage sur les exemples dupliqués)

Undersampling (RandomUnderSampler) : consiste à réduire le nombre d’exemples de la classe majoritaire (non-fumeurs).
(Inconvénient : perte d’une partie de l’information )


Nous avons retenu l’undersampling car notre dataset est assez grand pour que cette perte soit acceptable. Cette méthode a été appliquée uniquement sur l’échantillon d’entraînement, avant la recherche d’hyperparamètres par validation croisée, avec comme critère de score le recall.

#### Résultats : 


**LinearSVC**

### Modèle LinearSVC optimisé

Après une recherche d'hyperparamètres (GridSearchCV) centrée sur le **recall**, le modèle `LinearSVC` a atteint un **rappel de 93.5 %** sur le jeu de test. Ce résultat montre une excellente capacité à **ne pas rater les fumeurs**.

Le **F1-score de 0.71** confirme un bon équilibre général. La **précision plus faible (≈ 57 %)** traduit un nombre plus élevé de faux positifs, mais ce compromis est acceptable dans notre contexte, où il vaut mieux détecter trop de fumeurs que pas assez.

Ce modèle linéaire présente en plus l’avantage d’être **interprétable**, ce qui facilitera l’analyse des variables les plus influentes dans la décision.


**GradientBoostingClassifier**


Après optimisation du modèle `GradientBoostingClassifier` via une recherche d’hyperparamètres centrée sur le **recall**, nous avons obtenu un rappel de **91.4 %** sur le jeu de test. Ce résultat marque une **amélioration significative** par rapport au modèle initial (≈ 71.7 %) et démontre la capacité du modèle à **repérer efficacement les individus fumeurs**.

Bien que la précision ait légèrement baissé (~59 %), ce compromis est justifié dans le cadre de notre problématique, où l’enjeu principal est **d’éviter les faux négatifs**. Le **F1-score (≈ 0.72)** confirme un bon équilibre général entre les deux objectifs.



### Selection des variables :
### Sélection de variables avec LinearSVC

Afin de simplifier le modèle et d’améliorer son interprétabilité, nous avons appliqué une sélection automatique de variables à partir des poids du modèle `LinearSVC` optimisé. Cette étape a permis de réduire le nombre de variables explicatives de 24 à 12, en conservant uniquement les plus influentes.

Les résultats montrent une  baisse du **recall** (de 93,5 % à 72,4 %) mais une  amélioration de la **précision** (de 56,9 % à 64,9 %) et de l’**accuracy globale** (de 71,7 % à 75,5 %).





##### PARTIE INTERPRETATION 9 MAI ###############


Dans la suite de notre analyse, nous nous intéressons à l’interprétation des prédictions individuelles, aussi appelée explicabilité locale.
L’objectif est d'expliquer pourquoi le modèle a prédit qu’un individu était fumeur (ou non), en identifiant les variables qui ont le plus influencé cette prédiction.

## ICE
Les courbes ICE permettent d’analyser l’effet d’une variable spécifique sur la prédiction pour chaque individu.
Contrairement aux PDP  qui affichent la moyenne des effets, l’ICE trace une courbe par individu, révélant les variations individuelles

les courbes ICE permettent d’aller plus loin en explorant la variabilité interindividuelle derrière ces effets moyens :

Pour GTP, les courbes ICE confirment une relation croissante pour la majorité des individus. Toutefois, on observe que l’intensité de l’effet varie selon les personnes, certaines courbes étant plus plates ou plus abruptes que d’autres. Cela montre que l’impact de GTP n’est pas homogène dans toute la population.

Pour l’âge, les PDP suggéraient une relation non linéaire décroissante. Avec les courbes ICE on observe que de nombreuses courbes chutent fortement à partir d’un certain âge, confirmant que la majorité des individus âgés ont une probabilité prédite plus faible d’être fumeur. Mais d'autres courbes sont plus stables ou montrent un effet atténué, traduisant des profils atypiques : par exemple des fumeurs persistants parmi les personnes âgées.

Concernant les triglycérides, les ICE confirment une tendance ascendante relativement homogène, avec cependant quelques variations dans la pente, suggérant un effet plus marqué chez certains individus.

Et enfin pour ALT et AST montrent quant à elles une baisse globale des prédictions avec l’augmentation de ces enzymes, mais avec une dispersion faible. Cela pourrait indiquer que l’effet est plus stable ou moins influent, et pourrait refléter un phénomène indirect.


## Interprétation locale avec LIME

Afin de mieux comprendre les décisions de notre modèle Gradient Boosting pour un individu donné, nous avons utilisé la méthode LIME (Local Interpretable Model-agnostic Explanations).
Cette approche consiste à approximer localement le modèle complexe par un modèle linéaire plus simple, permettant d’identifier quelles variables influencent une prédiction spécifique.

Dans notre cas, nous avons utilisé un explainer en mode classification, en passant les données transformées (X_test_prepared), les noms des variables (feature_names) et les noms de classes (["non-fumeur", "fumeur"]).
Nous avons sélectionné l’individu d’index i = 10 de notre jeu de test, et généré une explication à l’aide de la fonction explain_instance


Parmi les résultats obtenus :

- Intercept : 0.0677 — c’est la probabilité moyenne d’être fumeur dans le voisinage généré par LIME
- Prediction_local : 0.7692 — c’est la prédiction du modèle simplifié (local)
- Right : 0.7855 — c’est la prédiction du modèle complexe (Gradient Boosting) pour cet individu

Ce résultat indique une prédiction de 78 % de probabilité d’être fumeur. Les variables qui ont le plus contribué à cette prédiction sont :
homme = 1 (poids : +0.48) : Être un homme a fortement poussé la prédiction vers "fumeur".
triglyceride > 0.40, hemoglobin > 0.61, tartar = 1, et une valeur intermédiaire de GTP ont également influencé le modèle dans ce sens, mais de manière plus modérée.

## Shape 

Voici une version corrigée et fluide de ton texte, sans redondance et structurée autour des deux graphiques SHAP :

---

### SHAP : interprétation locale et globale

Après avoir exploré LIME, nous utilisons ici la méthode SHAP, qui décompose chaque prédiction en une somme de contributions individuelles attribuées aux variables, selon une logique d’équité. Chaque variable "participe" à la prédiction et se voit attribuer une valeur SHAP indiquant dans quelle mesure elle augmente ou diminue la probabilité prédite.

Le **graphique Waterfall** représente l’explication locale pour un individu spécifique. La valeur moyenne des prédictions du modèle (appelée *base value*, ici -0.191 en log-odds) constitue le point de départ. À partir de là, chaque variable vient ajouter ou soustraire un effet pour aboutir à la prédiction finale, ici -0.293. Par exemple, le fait d’être un homme contribue fortement à augmenter la probabilité d’être fumeur (+0.88), tandis qu’un faible taux de GTP ou un âge élevé contribuent à réduire cette probabilité. On visualise ainsi clairement les forces "en présence" dans la décision du modèle.

Le **graphe SHAP beeswarm**, quant à lui, offre une vue globale sur l’influence des variables pour l’ensemble des prédictions. On observe que la variable `homme` est la plus influente, suivie par `Gtp`, `triglyceride`, `age` ou encore `ALT`. Les couleurs représentent la valeur de la variable : en rose pour les valeurs élevées, en bleu pour les faibles. Par exemple, un GTP ou un taux de triglycérides élevé pousse le modèle à prédire un statut de fumeur, tandis qu’un âge élevé contribue au contraire à diminuer cette probabilité.

Ces visualisations, nous permettent de mieux comprendre pourquoi un individu est classé comme fumeur (ou non) par le modèle, et d’identifier les facteurs personnels qui influencent le plus les prédictions.
