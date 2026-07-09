def trace(matrice:list[int])->int:
    if len(matrice)!=len(matrice[0]):
        raise ValueError
    t=0
    for i in range(len(matrice)):
        t+=matrice[i][i]
    return t

def determinant(matrice:list[list[int]]):
    colonne=len(matrice[0])
    lignes=len(matrice)
    if colonne==1 and lignes==1:
        return matrice[0][0]
    elif colonne==2 and lignes==2:
        return (matrice[0][0]*matrice[1][1])-(matrice[0][1]*matrice[1][0])
    elif colonne==3 and lignes==3:
        aei=(matrice[0][0]*matrice[1][1]*matrice[2][2])
        bfg=(matrice[0][1]*matrice[1][2]*matrice[2][0])
        cdh=(matrice[0][2]*matrice[1][0]*matrice[2][1])
        ceg=(matrice[0][2]*matrice[1][1]*matrice[2][0])
        bdi=(matrice[0][1]*matrice[1][0]*matrice[2][2])
        afh=(matrice[0][0]*matrice[1][2]*matrice[2][1])
        return aei+bfg+cdh-ceg-bdi-afh
    else:
        i=0
        s=0
        for j in range(colonne):
            sous_matrice = [
                [matrice[r][c] for c in range(colonne) if c != j]
                for r in range(1, lignes)
            ]
            s+=((-1)**(i+j))*matrice[i][j]*determinant(sous_matrice)
        return s
class matricePASinverse(Exception):
    pass
def inverse(matrice)->float:
    if determinant(matrice)==0:
        raise matricePASinverse("La matrice n'est pas inversible, car son déterminant est nul (det(A) = 0).")
    from operations import Transpose,multiplication_scalaire
    colonnes=len (matrice[0])
    lignes=len(matrice)
    comatrice=[[None for _ in range(colonnes)]for _ in range(lignes)]
    for i in range (lignes):
        for j in range(colonnes):
                sous_matrice = [
                    [matrice[r][c] for c in range(colonnes) if c != j]
                    for r in range(lignes) if r != i
                ]
                comatrice[i][j]=((-1)**(i+j))*determinant(sous_matrice)
    co_matrice_transpose=Transpose(comatrice)
    det_matrice=(1/determinant(matrice))
    matrice_inverse=multiplication_scalaire(co_matrice_transpose,det_matrice,1)
    return matrice_inverse
