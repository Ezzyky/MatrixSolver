from matrice_io import *
import sys

def clear_avec_msg(msg: str="Appuyez sur n'importe quel bouton pour sortir...")->None:
    import os
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

def options(sous_option:int,historique_list:list[str])->None:
        if sous_option==1:
            pass
        elif sous_option==2:
            historique(historique_list)
            clear_avec_msg()
        elif sous_option==3:
            infos()
            clear_avec_msg()
        elif sous_option==0:
            Quitter()