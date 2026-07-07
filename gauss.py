
from matrice_io import *

class seule_ligne(Exception):
    pass
def Reduction_de_Gauss(matrice: list[int])->list[int]:
    lignes=len(matrice)
    colonnes=len(matrice[0])
    if lignes>=2:
        ligne_courante = 0
        for colonne in range(colonnes):
            if ligne_courante >= lignes:
                break
            if matrice[ligne_courante][colonne] == 0:
                trouve = False
                for i in range(ligne_courante + 1, lignes):
                    if matrice[i][colonne] != 0:
                        matrice[ligne_courante], matrice[i] = matrice[i], matrice[ligne_courante]
                        print(f"\nL{ligne_courante+1} ↔ L{i+1}")
                        affichage(matrice)
                        trouve = True
                        break
                    if not trouve:
                        continue
            Operations_gauss_affichage(matrice, ligne_courante, colonne)
            ligne_courante += 1
            if ligne_courante < lignes and colonne < colonnes - 1:
                affichage(matrice)
                print()
    if lignes==1:
        raise seule_ligne("----> La matrice contient une seule ligne. Aucune élimination n'est nécessaire.")
    

