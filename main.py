def dataset_menu():
    ed


def ml_main():
    ed


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
