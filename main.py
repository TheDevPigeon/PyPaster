import os
import datetime
import pyperclip
import urllib.request
kill = False  #⬅️ NEVER CHANGE THIS


print(' /$$$$$$$            /$$$$$$$                       /$$                        ')
print('| $$__  $$          | $$__  $$                     | $$                        ')
print('| $$  \ $$ /$$   /$$| $$  \ $$ /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$ ')
print('| $$$$$$$/| $$  | $$| $$$$$$$/|____  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$')
print('| $$____/ | $$  | $$| $$____/  /$$$$$$$|  $$$$$$   | $$    | $$$$$$$$| $$  \__/')
print('| $$      | $$  | $$| $$      /$$__  $$ \____  $$  | $$ /$$| $$_____/| $$      ')
print('| $$      |  $$$$$$$| $$     |  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$      ')
print('|__/       \____  $$|__/      \_______/|_______/    \___/   \_______/|__/      ')
print('           /$$  | $$                                                           ')
print('          |  $$$$$$/                                                           ')
print('           \______/                                                            ')


while not kill:
    try:
        selection = ''
        
        # Menu and script selection
        print("\n  ╔══════════════════════════════════════════╗")
        print("  ║ 1 - Copier la date                       ║")
        print("  ║ 2 - Changer le nombre de cours           ║")
        print("  ║ 3 - Modifier l'emoji + copier date       ║")
        print("  ║ 4 - Fermer le programme                  ║")
        print("  ║ x - XXXXXXXXXXXXXXXXX                    ║")
        print("  ║ x - XXXXXXXXXXXXXXXXX                    ║")
        print("  ╚══════════════════════════════════════════╝")
        selection = input("Quel script ? Entre 1 et 4 : ")

        # Download my secret program (calulator)
        if selection == 'secret':
            url = "https://github.com/TheDevPigeon/PyPaster/archive/refs/heads/main.zip"
            zip_path = "PyPaster.zip"
            urllib.request.urlretrieve(url, zip_path)
            print("Téléchargement terminé, il est dans ce dossier")
            continue

        # Script selection 1 Copier la date
        if selection == '1':
            # Get today's date and format it
            date = datetime.date.today()
            date_formatee = date.strftime("%Y-%m-%d")
            
            # R/W nbrcours with OS Library
            file_name = 'nbrcours.txt'
            if not os.path.exists(file_name):
                with open(file_name, 'w') as file:
                    file.write('0')
            with open(file_name, 'r') as file:
                nbrcours = int(file.read().strip())
                nbrcours += 1
            with open(file_name, 'w') as file:
                file.write(str(nbrcours))
            
            # Pyperclip copy with nbrcours as string
            pyperclip.copy(date_formatee + " 😀 " + str(nbrcours))
            print('Voici le nombre de cours écoulé ', nbrcours)

        # Script selection 2 modifier nbrcours
        elif selection == '2':
            file_name = 'nbrcours.txt'
            if not os.path.exists(file_name):
                with open(file_name, 'w') as file:
                    file.write('0')

            # R/W nbrcours with OS Library
            with open(file_name, 'r') as file:
                nbrcours = int(file.read().strip())
            print(' Le nombre de cours est de : ' + str(nbrcours))
            bon = input('Est ce que le nombre de cours est correct ? (y/n) : ')
            if bon.lower() != 'y':
                nbrcours = int(input("Combien de cours a partir d'aujourd'hui ? : "))
                print('Le nombre de cours est maintenant de :', nbrcours)
                with open(file_name, 'w') as file:
                    file.write(str(nbrcours))

        # Script selection 3 Modifier l'emoji + copier date
        elif selection == '3':
            emojivoulu = input("Quel emoji voulez vous sur 5, 1 etant - et 5 etant + =====> ")  
            if emojivoulu == '1':
                emoji = " 🙁 "
            elif emojivoulu == '2':
                emoji = " 😕 "
            elif emojivoulu == '3':
                emoji = " 😐 "
            elif emojivoulu == '4':
                emoji = " 🙂 "
            else:
                emoji = " 😀 "

            print(emoji)

            # Get today's date and format it
            date = datetime.date.today()
            date_formatee = date.strftime("%Y-%m-%d")

            # R/W nbrcours with OS Library
            file_name = 'nbrcours.txt'
            if not os.path.exists(file_name):
                with open(file_name, 'w') as file:
                    file.write('0')
            with open(file_name, 'r') as file:
                nbrcours = int(file.read().strip())
                nbrcours += 1
            with open(file_name, 'w') as file:
                file.write(str(nbrcours))

            # Pyperclip copy with nbrcours as string
            pyperclip.copy(date_formatee + emoji + str(nbrcours))
            print('Voici le nombre de cours ====> ' + str(nbrcours))

        elif selection == '4':
            print("Fin du programme")
            kill = True

        else:
            pass

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

    finally:
        if kill:
            input("Appuyez sur Entrée pour fermer...")
