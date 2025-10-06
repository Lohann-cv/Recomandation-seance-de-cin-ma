import pandas as pd

df = pd.read_csv("diamonds.csv")
df = df[["carat", "cut", "color", "clarity", "price"]]


def shape_info():
    print(f"La shape du dataset utilisée est : {df.shape()}")


def average_carat_price():
    choice = input(
        "Quel valeur moyenne voulez vous ?\nCarat ou Prix? : ").lower
    if choice == "carat":
        average_carat = df["carat"]
        print(
            f"Le carat moyen des diamands de ce dataset est de : {average_carat.mean()}")
    if choice == "prix":
        average_price = df["price"]
        print(
            f"Le prix moyen des diamands de ce dataset est de {average_price.mean()}")
