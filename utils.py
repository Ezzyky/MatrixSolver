from matrice_io import *

def clear_avec_msg(msg: str="Appuyez sur n'importe quel bouton pour sortir...")->None:
    import os
    print(msg)
    input()
    os.system("cls" if os.name == "nt" else "clear")