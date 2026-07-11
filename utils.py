# Utilitaires d'interface, d'historique et de sauvegarde.
from menu_txtes import *
from matrice_io import *
from analyse import *
import sys
import os
import time

# Attend une confirmation de l'utilisateur puis efface l'écran.
def clear_avec_msg(msg: str="Appuyez sur n'importe quel bouton pour sortir...")->None:
    print(msg,end="")
    input()
    # Adapte la commande d'effacement au système d'exploitation.
    os.system("cls" if os.name == "nt" else "clear")

# Affiche les opérations enregistrées dans l'historique.
def historique(Historique:list[str])->None:
    # Distingue un historique vide d'une liste d'opérations à numéroter.
    if len(Historique) == 0:
        print("Aucune opération effectuée.")
    else:
        # La numérotation commence à 1 pour correspondre à l'affichage utilisateur.
        for i, operation in enumerate(Historique, start=1):
            print(f"{i}. {operation}")
        print()

# Affiche le message de fin et termine l'application.
def Quitter()->None:
    titre("""          Merci d'avoir utilisé notre application !
                    À bientôt !  Au revoir !""")
    sys.exit()
    clear_avec_msg()

# Date utilisée dans le nom des fichiers de sauvegarde.
time=time.strftime("%d-%m-%Y", time.localtime())
# Enregistre le résultat d'une opération dans un fichier texte daté.
def ecrire_dans_fichier(titre_operation:str, *elements)->None:
    # Le mode ajout conserve les sauvegardes antérieures et crée le fichier si nécessaire.
    with open(f"{time}.txt", "a+", encoding="utf-8") as f:
        f.write("="*60 + "\n")
        f.write(f"{titre_operation.center(60)}\n")
        f.write("="*60 + "\n\n")
        # Sérialise les matrices ligne par ligne pour préserver leur lisibilité.
        for nom, valeur in elements:
            f.write(f"{nom} :\n")
            # Les matrices sont détaillées ligne par ligne, contrairement aux valeurs simples.
            if isinstance(valeur, list): 
                for ligne in valeur:
                    f.write(str(ligne) + "\n")
            else: 
                f.write(str(valeur) + "\n")
            f.write("\n")
        f.write("="*60 +"\n\n")

# Traite les actions proposées après l'affichage d'un résultat.
def options(historique_list: list[str],fun_de_infos, titre_operation: str=None, *elements)->None:
        # Valide la saisie avant d'exécuter une action associée à l'option.
        try:
            sous_option = int(input("Choisissez une option : "))
        except ValueError:
            clear_avec_msg("Option invalide.")
            return
        # Nettoie l'écran avant d'afficher le contenu associé au choix.
        os.system("cls")
        print("\033[H", end="")

        # Oriente l'utilisateur vers la sauvegarde, l'historique ou l'aide contextuelle.
        if sous_option==1:          
                titre("Done")
                ecrire_dans_fichier(titre_operation, *elements)
                clear_avec_msg()
        elif sous_option==2:
                titre("Historique")
                historique(historique_list)
                clear_avec_msg()
        elif sous_option==3:
                fun_de_infos()
                clear_avec_msg()
        elif sous_option==0:
                os.system("cls" if os.name == "nt" else "clear")
        else:
                os.system("cls" if os.name == "nt" else "clear")
            
