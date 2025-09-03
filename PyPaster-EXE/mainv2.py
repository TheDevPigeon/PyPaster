import os
import time
import datetime
import pyperclip
nbr = input("Quel script ? Entre 1 et 4 : ") 

file_name = 'nbrcours.txt'

if os.path.exists(file_name):
    # Si le fichier existe, lire la valeur actuelle
    with open(file_name, 'r') as file:
        nbrcours = int(file.read().strip())
else:
    # Si le fichier n'existe pas, initialiser la variable
    nbrcours = 0

# Incrémenter la variable
nbrcours += 1

# Afficher la valeur incrémentée
print(f"Le nombre de cours est : {nbrcours}")

# Enregistrer la nouvelle valeur dans le fichier
with open(file_name, 'w') as file:
    file.write(str(nbrcours))

if nbr == '1':
        aujourdhui = datetime.date.today()
        date_formatee = aujourdhui.strftime("%Y-%m-%d")
        pyperclip.copy(date_formatee + " 😀" + nbrcours) 
        print('La date a été copiée')
elif nbr == '2':
        
        print('Nombre de cour actuel :', nbrcours)
        correct = input('Est ce que le nombre de cours est correct ? (y/n) : ')
        if correct == 'y':
                pass
        else:
                nbrcours = input("Combien de cours a partir daujourdhui ? : ")
                print('Le nombre de cours est maintenant de :', nbrcours)
elif nbr == '3': 
        pass

file_name = 'nbrcours.txt'

