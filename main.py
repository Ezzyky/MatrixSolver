from functions import *
matrice=prenant_matrice()
lignes=len(matrice)
colonnes=len(matrice[0])
print(affichage(matrice))
# Permutation des lignes L1 et la première ligne dont le premier élément est non nul
index=0
if lignes>=2:
    if matrice[0][0]==0:

        for i in range(lignes):
            if matrice[i][0]!=0:
                index=i
                break

        for i in range(colonnes):
            temp=matrice[0][i]
            matrice[0][i]=matrice[index][i]
            matrice[index][i]=temp
        print(f"L1 ​↔ L​{index+1}")
        affichage(matrice)
for pivot in range(min(len(matrice), len(matrice[0]))):
    elimination_gauss(matrice, pivot)
    print(f"")")
    affichage(matrice)
    print()

        













# if matrice[0][0]!=0:
#     for j in range(1,lignes):
#         for i in range (colonnes):
#             if matrice[j][0]!=0:
#                 a= matrice[j][0]
#                 for i in range(colonnes):
#                     matrice[j][i] = (matrice[j][i] * matrice[0][0]- matrice[0][i] * a)
