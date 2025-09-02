import os
import datetime
import pyperclip

file_name = 'nbrcours.txt'

if os.path.exists(file_name):
    try:
        with open(file_name, 'r') as file:
            nbrcours = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        nbrcours = 0
else:
    nbrcours = 0

def menu():
    print("\n  ╔══════════════════════════════════════════╗")
    print("  ║ 1 - Copier la date                       ║")
    print("  ║ 2 - Changer le nombre de cours           ║")
    print("  ║ 3 - Retourner au menu                    ║")
    print("  ╚══════════════════════════════════════════╝")
    return input("Quel script ? Entre 1 et 4 : ")

nbr = input("Quel script ? Entre 1 et 3 : ")


if nbr == '1':
        nbrcours += 1
        date = datetime.date.today()
        date_formatee = date.strftime("%Y-%m-%d")
        pyperclip.copy(date_formatee + " 😀" + str(nbrcours))
        print('La date a été copiée')
        with open(file_name, 'w') as file:
            file.write(str(nbrcours))  
            menu()
elif nbr == '2':
        print('Nombre de cour actuel :', nbrcours)
        correct = input('Est ce que le nombre de cours est correct ? (y/n) : ')
        if correct.lower() != 'y':
            try:
                nbrcours = int(input("Combien de cours a partir d'aujourd'hui ? : "))
                print('Le nombre de cours est maintenant de :', nbrcours)
                with open(file_name, 'w') as file:
                    file.write(str(nbrcours))
            except ValueError:
                print("Cela n'a pas marché :(")
elif nbr == '3':
        print("Fin du programme.")
        pass
else:
        print("Choix invalide. Veuillez choisir entre 1, 2 ou 3.")
