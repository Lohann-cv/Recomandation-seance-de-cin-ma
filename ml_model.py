import sklearn
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib as plt
import numpy as np

diamonds = pd.read_csv("diamonds.csv")
diamonds = diamonds[["carat", "cut", "color", "clarity", "price"]]
# Peu commun sont ces commande mais cela est du à une mise à jours pandas
cut_map = {"Ideal": 1, "Premium": 2, "Very Good": 3, "Good": 4, "Fair": 5}
color_map = {"D": 1, "E": 2, "F": 3, "G": 4, "H": 5, "I": 6, "J": 7}
clarity_map = {
    "IF": 0,
    "VVS1": 1,
    "VVS2": 2,
    "VS1": 3,
    "VS2": 4,
    "SI1": 5,
    "SI2": 6,
    "I1": 7
}

diamonds["cut"] = diamonds["cut"].map(cut_map).astype(int)
diamonds["color"] = diamonds["color"].map(color_map).astype(int)
diamonds["clarity"] = diamonds["clarity"].map(clarity_map).astype(int)

y = diamonds["price"]
X = diamonds.drop("price", axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = KNeighborsRegressor(n_neighbors=3)
model.fit(X_train, y_train)
print("Train score:", model.score(X_train, y_train))
print("Test score:", model.score(X_test, y_test))


def prediction():
    user_carat = float(input("Veuillez saisir le carat : "))
    user_cut = int(input(
        "Veuillez saisir le cut de votre diamand,\n1-Ideal, 2-Premium, 3-Very Good, 4-Good, 5-Fair : "))
    user_color = int(input(
        "Veuillez saisir la color de votre diamand,\n1-D, 2-E, 3-F, 4-G, 5-H, 6-I, 7-J : "))
    user_clarity = int(input(
        "Veuillez saisir la clarity de votre diamand,\n1-IF, 2-VVS1, 3-VVS2, 4-VS1, 5-VS2, 6-Sl1, 7-Sl2, 8-I1 : "))
    user_diamond = pd.DataFrame([[user_carat, user_cut, user_color, user_clarity]], columns=[
                                "carat", "cut", "color", "clarity"])
    print(
        f"le prix de votre diamand est de {model.predict(user_diamond)[0]:2f}€.")
