def print_message_de_bienvenue():
    print("Bienvenue sur le petit-calculateur !")

def input_deux_nombres():
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    return num1, num2

def print_menu_et_obtenir_choix():
    print("=== MENU ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    user_choice = input("Entrez votre choix (1-4) : ")
    while user_choice not in ["1", "2", "3", "4"]:
        user_choice = input("Choix invalide. Entrez votre choix (1-4) : ")
    return user_choice

def somme(num1, num2):
    return num1 + num2

def soustraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Erreur : division par zéro")

def effectuer_calcul(choix_utilisateur):
    num1, num2 = input_deux_nombres()
    match choix_utilisateur:
        case '1':
            resultat = somme(num1, num2)
        case '2':
            resultat = soustraction(num1, num2)
        case '3':
            resultat = multiplication(num1, num2)
        case '4':
            resultat = division(num1, num2)
        case _:
            print("Choix invalide.")
    return resultat

if __name__ == '__main__':
    print_message_de_bienvenue()
    while True:
        choix_utilisateur = print_menu_et_obtenir_choix()
        resultat = effectuer_calcul(choix_utilisateur)
        print("Le résultat est :", resultat)

        continuation_choix = input("Appuyez sur 'a' pour continuer ou 'o' pour quitter : ")
        if continuation_choix.lower() == 'o':
            break
        elif continuation_choix.lower() != 'a':
            continue



