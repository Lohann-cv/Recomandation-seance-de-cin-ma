import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import numpy as np

# Chargement dataset
try:
    diamonds = pd.read_csv("diamonds.csv")
    diamonds = diamonds[["carat", "cut", "color", "clarity", "price"]]
except FileNotFoundError:
    print("Erreur : Le fichier 'diamonds.csv' est introuvable.")
    exit()
except Exception as e:
    print(f"Une erreur est survenue lors du chargement du fichier : {e}")
    exit()

# Mapping des variables catégorielles
cut_map = {"Ideal": 1, "Premium": 2, "Very Good": 3, "Good": 4, "Fair": 5}
color_map = {"D": 1, "E": 2, "F": 3, "G": 4, "H": 5, "I": 6, "J": 7}
clarity_map = {
    "IF": 1,
    "VVS1": 2,
    "VVS2": 3,
    "VS1": 4,
    "VS2": 5,
    "SI1": 6,
    "SI2": 7,
    "I1": 8
}

try:
    diamonds["cut"] = diamonds["cut"].map(cut_map).astype(int)
    diamonds["color"] = diamonds["color"].map(color_map).astype(int)
    diamonds["clarity"] = diamonds["clarity"].map(clarity_map).astype(int)
except Exception as e:
    print(f"Erreur lors du mapping des colonnes : {e}")
    exit()

# Préparation données
y = diamonds["price"]
X = diamonds.drop("price", axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Entraînement modèle
model = KNeighborsRegressor(n_neighbors=3)
model.fit(X_train, y_train)
print("Train score:", model.score(X_train, y_train))
print("Test score:", model.score(X_test, y_test))


def prediction():
    try:
        user_carat = float(input("Veuillez saisir le carat : "))
        user_cut = int(input(
            "Veuillez saisir le cut de votre diamant,\n1-Ideal, 2-Premium, 3-Very Good, 4-Good, 5-Fair : "))
        user_color = int(input(
            "Veuillez saisir la color de votre diamant,\n1-D, 2-E, 3-F, 4-G, 5-H, 6-I, 7-J : "))
        user_clarity = int(input(
            "Veuillez saisir la clarity de votre diamant,\n1-IF, 2-VVS1, 3-VVS2, 4-VS1, 5-VS2, 6-SI1, 7-SI2, 8-I1 : "))

        # Vérificatio values
        if not (1 <= user_cut <= 5):
            raise ValueError("Cut invalide.")
        if not (1 <= user_color <= 7):
            raise ValueError("Color invalide.")
        if not (1 <= user_clarity <= 8):
            raise ValueError("Clarity invalide.")

        user_diamond = pd.DataFrame([[user_carat, user_cut, user_color, user_clarity]],
                                    columns=["carat", "cut", "color", "clarity"])
        predicted_price = model.predict(user_diamond)[0]
        print(
            f"Le prix estimé de votre diamant est de {predicted_price:.2f} €.")
    except ValueError as ve:
        print(f"Erreur de saisie : {ve}")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
