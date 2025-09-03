import os
import time
import datetime
import pyperclip


def script_copier_date():

    print("\n--- Copie de la date ---")
    try:
        aujourdhui = datetime.date.today()
        date_formatee = aujourdhui.strftime("%Y-%m-%d")
        pyperclip.copy(date_formatee)
        print(f"✅ Succès! La date '{date_formatee}' a été copiée.")
    except pyperclip.PyperclipException:
        print("❌ Erreur: Pyperclip n'a pas pu accéder au presse-papiers.")
        print("   Veuillez vous assurer qu'un gestionnaire de presse-papiers est installé (ex: xclip sur Linux).")

def script_placeholder_2():
    """Un script d'exemple qui ne fait rien de spécial."""
    print("\n--- Lancement du Script 2: Placeholder ---")
    print("Ce script est un exemple. Remplacez son contenu par ce que vous voulez!")
    for i in range(3):
        print(f"Action en cours... {i+1}/3")
        time.sleep(0.5) # Pause de 0.5 seconde
    print("✅ Tâche terminée.")

def script_placeholder_3():
    """Un autre script d'exemple."""
    print("\n--- Lancement du Script 3: Autre Placeholder ---")
    print("Voici un autre exemple de script que vous pouvez personnaliser.")
    print("✅ Tâche terminée.")

# --- Fonctions du Menu ---

def afficher_menu():
    """Affiche les options du menu principal."""
    # os.system('cls' if os.name == 'nt' else 'clear') # Décommentez pour effacer l'écran
    print("\n  ╔══════════════════════════════════════════╗")
    print("  ║              MENU PRINCIPAL              ║")
    print("  ╠══════════════════════════════════════════╣")
    print("  ║ 1. Copier la date dans le presse-papiers ║")
    print("  ║ 2. Lancer le script N°2 (Exemple)        ║")
    print("  ║ 3. Lancer le script N°3 (Exemple)        ║")
    print("  ║ 4. Quitter le programme                  ║")
    print("  ╚══════════════════════════════════════════╝")

def main():
    while True:
        afficher_menu()
        choix = input("Ecrit un chiffre de 1 a 4 pour selectionner un script")

        if choix == '1':
            script_copier_date()
        elif choix == '2':
            script_placeholder_2()
        elif choix == '3':
            script_placeholder_3()
        elif choix == '4':
            print("\nAu revoir")
            break 
        else:
            print("\nEntre 1 et 4.")


        input("\nAppuie sur Entrée pour retourner")


if __name__ == "__main__":
    main()