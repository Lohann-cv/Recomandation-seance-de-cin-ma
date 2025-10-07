import sklearn
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import matplotlib as plt
import numpy as np

diamonds = pd.read_csv("diamonds.csv")
print(diamonds.head())
diamonds = diamonds[["carat", "cut", "color", "clarity", "price"]]
print(diamonds.head(30))
diamonds["cut"] = diamonds["cut"].rename(
    ["Ideal", "Premium", "Very Good", "Good", "Fair"], ["1", "2", "3", "4", "5"])
print(diamonds.head(30))
model = KNeighborsClassifier()
