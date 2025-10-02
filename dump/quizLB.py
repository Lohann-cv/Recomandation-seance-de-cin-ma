
def action():
    while True:
        choix2 = input(
            "FastAndFurious, d'accord, prochaine question !\n1. Mission: Impossible - The Final Reckoning, 2. Avenger End Game ou 3. Rocky\nEt maintenant ? 1, 2 ou 3 : ")
        if choix2 == 1:
            action_fan()
        elif choix2 == 2:
            superhero()
        elif choix2 == 3:
            sport_fan()
        else:
            print("Veuiller rentrer une valeur numérique !")
            return


def quiz():
    while True:
        print("====Le LettreBoite quiz====\nUne série de question va vous être possé où vous allez devoir choisir votre préférer parmis 3 films !\nEnsuite il sera déduit un film qui peut vous plaire\n(Pour choisir un film rentrer son index numérique dans la réponse)")
        choix1 = input(
            "1. FastAndFurious, 2. Openheimer ou 3. Qu'es qu'on a fait au bon Dieu ?\nAlors ? 1, 2 ou 3 : ")
        if choix1 == 1:
            action()
        elif choix1 == 2:
            great_movie()
        elif choix1 == 3:
            comedy()
        else:
            print("Veuiller rentrer une valeur numérique !")
            return
