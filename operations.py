def multiplication_scalaire(matrice:list[int],scalaire:float,flag:int=0)->float:
    matrice_m=[[None for i in range(len(matrice[0]))]for i in range(len(matrice))]
    if flag==0:
        print("Calcul de la multiplication par le scalaire :")
        print()
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            matrice_m[i][j]=scalaire*matrice[i][j]
            if flag==0:
                print(f"{matrice[i][j]} X {scalaire:.1f}  ",end="")
                print()
    return matrice_m

def addition(matrice1:list[int],matrice2:list[int])->list[int]:
    matrice_add=[[None for i in range(len(matrice2[0]))]for i in range(len(matrice2))]
    for i in range(len(matrice1)):
        for j in range(len(matrice2[0])):
            matrice_add[i][j]=matrice1[i][j]+matrice2[i][j]
            print(f"{matrice1[i][j]} + {matrice2[i][j]}  ",end="")
            print()
    return matrice_add

def souetraction(matrice1:list[int],matrice2:list[int])->list[int]:
    matrice_souetraction=[[None for i in range(len(matrice2[0]))]for i in range(len(matrice2))]
    for i in range(len(matrice1)):
        for j in range(len(matrice2[0])):
            matrice_souetraction[i][j]=matrice1[i][j]-matrice2[i][j]
            print(f"{matrice1[i][j]}-{matrice2[i][j]}  ",end="")
            print()
    return matrice_souetraction

def multiplication(matrice1:list[int],matrice2:list[int],flag:int=0)->list[int]:
            matrice_multi=[[0 for i in range(len(matrice2[0]))]for i in range(len(matrice1))]
            for i in range(len(matrice1)):
                for j in range(len(matrice2[0])):
                    for k in range(len(matrice2)):
                        matrice_multi[i][j] += matrice1[i][k] * matrice2[k][j]
                        if flag==1:
                            print(f"{matrice1[i][k]} X {matrice2[k][j]}")
            return matrice_multi

def Transpose(matrice:list[int])->list[int]:
    lignes=len(matrice)
    colones=len(matrice[0])
    matrice_Transpose=[[None for i in range(lignes)]for i in range(colones)]
    for i in range(lignes):
        for j in range(colones):
            matrice_Transpose[j][i]=matrice[i][j]
    return matrice_Transpose

class ErrorNegative(Exception):
    pass


def puissance_matrice(matrice:list[list[int]],N:int)->list[list[int]]:
    if N<0:
        raise ErrorNegative("----> La puissance doit être positive ou nulle.")
    if N==0:
        taille = len(matrice)
        return [[1 if i == j else 0 for j in range(taille)] for i in range(taille)]
    if N==1:
        print()
        return matrice
    resulta=matrice
    for _ in range(N-1):
        resulta=multiplication(resulta,matrice)
    return resulta