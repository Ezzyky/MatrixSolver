
# Algorithmes de réduction de matrices par élimination de Gauss.
from matrice_io import *

# Exception levée lorsqu'aucune élimination n'est nécessaire.
class seule_ligne(Exception):
    pass
# Réduit une matrice en éliminant les éléments sous chaque pivot.
def Reduction_de_Gauss(matrice: list[int],flag:int=0)->list[int]:
    lignes=len(matrice)
    colonnes=len(matrice[0])
    # La réduction n'a de sens que si plusieurs lignes peuvent être comparées.
    if lignes>=2:
        # Ligne dans laquelle sera placé le prochain pivot.
        ligne_courante = 0
        # Balaye les colonnes de gauche à droite pour construire les pivots successifs.
        for colonne in range(colonnes):
            # Arrête le parcours lorsque toutes les lignes ont reçu un pivot.
            if ligne_courante >= lignes:
                break
            # Recherche une ligne de remplacement lorsque le pivot est nul.
            if matrice[ligne_courante][colonne] == 0:
                trouve = False
                for i in range(ligne_courante + 1, lignes):
                    if matrice[i][colonne] != 0:
                        # L'échange rend le pivot exploitable sans changer l'ensemble des solutions.
                        matrice[ligne_courante], matrice[i] = matrice[i], matrice[ligne_courante]
                        if flag==0:
                            print(f"\nL{ligne_courante+1} ↔ L{i+1}")
                            affichage(matrice)
                        trouve = True
                        break
                    if not trouve:
                        continue
            # Annule les coefficients situés sous le pivot retenu.
            Operations_gauss_affichage(matrice, ligne_courante, colonne,1)
            ligne_courante += 1
            if flag==0:
                if ligne_courante < lignes and colonne < colonnes - 1:
                    affichage(matrice)
                    print()
    # Signale explicitement le cas où aucune élimination n'est possible.
    if lignes==1:
        raise seule_ligne("----> La matrice contient une seule ligne. Aucune élimination n'est nécessaire.")
    
def rang(matrice:list[list[float]])->int:
    Reduction_de_Gauss(matrice,1)
    lignes=len(matrice)
    colonnes=len(matrice[0])
    rg=0
    for i in range(lignes):
        s=0
        for j in range(colonnes):
            if matrice[i][j]!=0:
                s+=1
        if s!=colonnes:
            rg+=1
    return rg
