from menu_txtes import *
import sys
import os
import time

def clear_avec_msg(msg: str="Appuyez sur n'importe quel bouton pour sortir...")->None:
    print(msg)
    input()
    os.system("cls" if os.name == "nt" else "clear")

def historique(Historique:list[str])->None:
    if len(Historique) == 0:
        print("Aucune opération effectuée.")
    else:
        for i, operation in enumerate(Historique, start=1):
            print(f"{i}. {operation}")

def Quitter()->None:
    titre("""          Merci d'avoir utilisé notre application !
                    À bientôt !  Au revoir !""")
    sys.exit()
    clear_avec_msg()

time=time.strftime("%d-%m-%Y", time.localtime())
def ecrire_dans_fichier(titre_operation:str, *elements)->None:
    with open(f"{time}.txt", "a+", encoding="utf-8") as f:
        f.write("="*60 + "\n")
        f.write(f"{titre_operation.center(60)}\n")
        f.write("="*60 + "\n\n")
        for nom, valeur in elements:
            f.write(f"{nom} :\n")
            if isinstance(valeur, list): 
                for ligne in valeur:
                    f.write(str(ligne) + "\n")
            else: 
                f.write(str(valeur) + "\n")
            f.write("\n")
        f.write("="*60 + "\n\n")

def options(historique_list: list[str],fun_de_infos, titre_operation: str, *elements)->None:
        try:
            sous_option = int(input("Choisissez une option : "))
        except ValueError:
            clear_avec_msg("Option invalide.")
            return
        os.system("cls")
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