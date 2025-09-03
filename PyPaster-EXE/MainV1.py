import os
import time
import datetime
import pyperclip

def main(): 
    while True:
        affichermenu()
        choix = input("Choisit le script, entre 1 et 4 : ")

        if choix == '1':
            copierdate()
        elif choix == '2':
            nbrcours() 
        elif choix == '3':
            pass
        else:
            print("Un nombre entre 1 et 4 poto")

def affichermenu():
    print("\n  ╔══════════════════════════════════════════╗")

def copierdate():
    print("\n--- Copie de la date ---")

def nbrcours():
    print







if __name__ == "__main__":
    main()