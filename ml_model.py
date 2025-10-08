import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib as plt
import numpy as np

diamonds = pd.read_csv("diamonds.csv")
print(diamonds.head())
diamonds = diamonds[["carat", "cut", "color", "clarity", "price"]]
print(diamonds.head(30))
diamonds["cut"] = diamonds["cut"].replace(
    {"Ideal": 1, "Premium": 2, "Very Good": 3, "Good": 4, "Fair": 5}
)
diamonds['color'] = diamonds["color"].replace(
    {"D": 1, "E": 2, "F": 3, "G": 4, "H": 5, "I": 6, "J": 7}
)
diamonds['clarity'] = diamonds["clarity"].replace(
    {"VVS2": 1, "VS1": 2, "VS2": 3, "Sl1": 4, "Sl2": 5}
)


y = diamonds["price"]
X = diamonds.drop("price", axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)
print("Train score:", model.score(X_train, y_train))
print("Test score:", model.score(X_test, y_test))
