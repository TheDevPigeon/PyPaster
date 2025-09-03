import pyperclip
import datetime
import os 
nbrcours = 0
selection = input('Copier la date ? y/n ====>')
file_name = 'nbrcours.txt'


if selection.lower == ('y'):
    date = datetime.date.today()
    date_formatee = date.strftime("%Y-%m-%d")
    pyperclip.copy(date_formatee + " 😀", (nbrcours))
    print('La date a été copiée')
    file_name = 'nbrcours.txt'
    os.path.exists(file_name)
    with open(file_name, 'r') as file:
        nbrcours = int(file.read().strip())
        nbrcours += 1
    with open(file_name, 'w') as file:
        file.write(str(nbrcours))