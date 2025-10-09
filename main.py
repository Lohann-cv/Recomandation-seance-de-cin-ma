import dataset as ds
import sys
import ml_model


def quit_or_stay():
    sys.exit() if input("1=continuer, 2=quiter le programe : ") == "2" else None


def dataset_menu():
    while True:
        print("===Menu information dataset===\n1- Shape du dataset\n2- Moyenne du dataset\n3- Maximum et minimum des diamands du dataset\n4- Quitter")
        choice = input(
            "Veuillez rentrer la valeur numérique de votre option choisie : ")
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
            print("Aurevoir et bonne journée !")
            break
        else:
            print("Veuillez rentrer 1, 2, 3 ou 4 selon votre option choisie !")
            return


def ml_main():
    print("Nous allons vous demander de rentrer les diverses information de votre diamand pour pouvoir déduire son prix,merci de rentrer les valeurs numerique associer")
    ml_model.prediction()
    quit_or_stay()


def menu():
    while True:
        print("Bonjour, choisisez ce que vous voulez faire aujourd'hui :\n1- Recherche du prix d'un diamand en fonction de ces carateristique\n2- Information relative à notre dataset\n3- Quiter")
        choice = input(
            "Veuillez rentrer la valeur numérique de votre option choisie : ")
        if choice == "1":
            ml_main()
        elif choice == "2":
            dataset_menu()
        elif choice == "3":
            print("Aurevoir et bonne journée !")
            break
        else:
            print("Veuillez rentrer 1, 2 ou 3 selon votre option choisie !")
            return


menu()
