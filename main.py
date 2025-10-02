

def menu():
    while True:
        print("====Menu lettreboite====\nChoisisez ce que vous voulez faire ajourd'hui\n1. Questionaire de film\n2. Mes réponses au questionaire\n3. Mes filmes conseiller\n4. Quitter lettreboite")
        choix = input("Rentrer le numéro de l'action que vous voulez faire : ")

        if choix == 1:
            qz.quiz()
        elif choix == 2:
            quiz_answers()
        elif choix == 3:
            recommended_films()
        elif choix == 4:
            print("Agréable journée à vous")
            break
        else:
            print("Merci de bien rentrer la valeur numérique coréspondant à votre choix")
            return


menu()
