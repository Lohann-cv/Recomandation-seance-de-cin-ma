import pandas as pd

try:
    df = pd.read_csv("diamonds.csv")
    df = df[["carat", "cut", "color", "clarity", "price"]]
except FileNotFoundError:
    print("Erreur : Le fichier 'diamonds.csv' est introuvable.")
    exit()
except Exception as e:
    print(f"Une erreur est survenue lors du chargement du fichier : {e}")
    exit()


def max_min_price():
    try:
        choice = input(
            "Voulez-vous savoir les informations du diamant le plus cher ou le moins cher ? Choisissez 'maximum' ou 'minimum' : "
        ).lower()
        if choice == "maximum":
            max_diamond = df["price"].max()
            print(
                f"Les informations du diamant le plus cher valant {max_diamond} sont :\n{df.loc[df['price'] == max_diamond]}"
            )
        elif choice == "minimum":
            min_diamond = df["price"].min()
            print(
                f"Les informations du diamant le moins cher valant {min_diamond} sont :\n{df.loc[df['price'] == min_diamond]}"
            )
        else:
            print("Veuillez rentrer 'maximum' ou 'minimum' !")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")


def average_carat_price():
    try:
        choice = input(
            "Quelle valeur moyenne voulez-vous ? 'carat' ou 'prix' : "
        ).lower()
        if choice == "carat":
            average_carat = df["carat"]
            print(
                f"Le carat moyen des diamants de ce dataset est de : {average_carat.mean():.2f}"
            )
        elif choice == "prix":
            average_price = df["price"]
            print(
                f"Le prix moyen des diamants de ce dataset est de : {average_price.mean():.2f}"
            )
        else:
            print("Veuillez rentrer 'carat' ou 'prix' !")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")


def shape_info():
    try:
        print(f"La shape du dataset utilisée est : {df.shape}")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
