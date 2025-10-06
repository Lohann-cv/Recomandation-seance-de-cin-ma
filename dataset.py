import pandas as pd

df = pd.read_csv("diamonds.csv")
df = df[["carat", "cut", "color", "clarity", "price"]]


def shape_info():
    print(f"La shape du dataset utilisée est : {df.shape}")


def average_carat_price():
    choice = input(
        "Quel valeur moyenne voulez vous ?\nCarat ou Prix? : ").lower()
    if choice == "carat":
        average_carat = df["carat"]
        print(
            f"Le carat moyen des diamands de ce dataset est de : {average_carat.mean()}")
    elif choice == "prix":
        average_price = df["price"]
        print(
            f"Le prix moyen des diamands de ce dataset est de {average_price.mean()}")
    else:
        print("Veuiller rentrer 'carat' ou 'price' !")
        return


def max_min_price():
    choice = input(
        "Voulez vous savoir les informations du diamand le plus cher ou le moins cher? Choisisez Maximum ou Minimum : ").lower()
    if choice == "maximum":
        max_diamond = df["price"].max()
        print(
            f"Les informations du diamand le plus cher valant {max_diamond} sont :\n{df.loc[df['price'] == max_diamond]}")
    elif choice == "minimum":
        min_diamond = df["price"].min()
        print(
            f"Les informations du diamand le moins cher valant {min_diamond} sont :\n{df.loc[df['price'] == min_diamond]}")
    else:
        print("Veuillez rentrer 'maximum' ou 'minimum' !")
        return
