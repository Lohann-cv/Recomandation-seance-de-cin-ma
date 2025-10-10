import dataset as ds
import sys
import ml_model


def quit_or_stay():
    try:
        choice = input("1 = Continuer | 2 = Quitter le programme : ")
        if choice == "2":
            print("Programme terminé. À bientôt !")
            sys.exit()
        elif choice != "1":
            print("Entrée invalide. Retour au menu.")
    except Exception as e:
        print(f"Erreur : {e}")


def dataset_menu():
    while True:
        print("\n=== Menu Information Dataset ===")
        print("1 - Shape du dataset")
        print("2 - Moyenne du dataset")
        print("3 - Maximum et minimum des diamants du dataset")
        print("4 - Retour au menu principal")

        choice = input("Veuillez entrer le numéro de votre choix : ")
        try:
            if choice == "1":
                ds.shape_info()
                quit_or_stay()
            elif choice == "2":
                ds.average_carat_price()
                quit_or_stay()
            elif choice == "3":
                ds.max_min_price()
                quit_or_stay()
            elif choice == "4":
                break
            else:
                print("Veuillez entrer un chiffre entre 1 et 4.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")


def ml_main():
    print("\n=== Estimation du prix d'un diamant ===")
    print("Veuillez entrer les caractéristiques numériques de votre diamant.")
    try:
        ml_model.prediction()
    except Exception as e:
        print(f"Erreur lors de la prédiction : {e}")
    quit_or_stay()


def menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1 - Estimer le prix d'un diamant")
        print("2 - Informations sur le dataset")
        print("3 - Quitter")

        choice = input("Veuillez entrer le numéro de votre choix : ")
        try:
            if choice == "1":
                ml_main()
            elif choice == "2":
                dataset_menu()
            elif choice == "3":
                print("Merci et à bientôt !")
                break
            else:
                print("Veuillez entrer 1, 2 ou 3.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")


menu()
