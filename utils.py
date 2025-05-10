import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
from sklearn.inspection import partial_dependence, PartialDependenceDisplay, permutation_importance


## fonction de winzorisation

def winsorize_data(xtrain, xtest, feature):

    """_summary_

    Fonction permettant de winsorizez un jeu d'entrainement et de test en calculant
    les quantiles sur le jeu d'entrainement et l'appliquant sur le jeu test.

    Pour se prémunir d'un data leak.
    
    """
    
    # Définir les quantiles sur xtrain
    lower_quantile = 0.010  # 1% quantile
    upper_quantile = 0.99  # 99% quantile

    # Calcul des bornes à partir des quantiles sur xtrain
    lower_bound = np.quantile(xtrain[feature], lower_quantile)
    upper_bound = np.quantile(xtrain[feature], upper_quantile)

    # Appliquer la winsorisation sur xtrain
    xtrain_winsorized = np.clip(xtrain[feature], lower_bound, upper_bound)

    # Appliquer les mêmes bornes sur xtest
    xtest_winsorized = np.clip(xtest[feature], lower_bound, upper_bound)

    return(xtrain_winsorized, xtest_winsorized)



## Fonction pour détecter les types 

def detect_variable_types(df):
    types = {
        "numerical": [],
        "categorical": [],
        "datetime": [],
        "boolean": [],
        "others": []
    }

    for col in df.columns:
        if pd.api.types.is_bool_dtype(df[col]):  # mettre ce test en premier
            types["boolean"].append(col)
        elif pd.api.types.is_numeric_dtype(df[col]):
            types["numerical"].append(col)
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            types["datetime"].append(col)
        elif pd.api.types.is_object_dtype(df[col]) or pd.api.types.is_categorical_dtype(df[col]):
            types["categorical"].append(col)
        else:
            types["others"].append(col)

    return types


# # Calculer le PDP sur les données standardisées

def display_original_pdp_values(num_col, model, df, scaler, feature_names):
    """
    Affiche le PDP avec les valeurs originales (inversées après scaling)
    
    Args:
        num_col (int): index de la variable dans les features numériques
        model: modèle déjà entraîné
        df: X transformé uniquement avec les colonnes numériques (après scaling)
        scaler: le StandardScaler utilisé sur les données
        feature_names (list): noms des colonnes dans le même ordre que df
    """
    features_to_plot = [(num_col,)]  # PDP sur une seule feature
    
    pdp_results = partial_dependence(model, df, features=features_to_plot, kind='average')

    # Grille de valeurs standardisées et PDP associées
    grid = pdp_results['grid_values'][0]
    pdp = pdp_results['average'][0]

    # Inverser la standardisation
    original_grid = scaler.mean_[num_col] + grid * scaler.scale_[num_col]

    # Affichage
    plt.figure(figsize=(4, 3))
    plt.plot(original_grid, pdp)
    plt.xlabel(f"Variable : {feature_names[num_col]}")
    plt.ylabel("Partial dependence")
    plt.title("Original Partial Dependence Plot")
    plt.grid(True)
    plt.tight_layout()
    plt.show()



