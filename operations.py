def multiplication_scalaire(matrice:list[int],scalaire:float)->float:
    matrice_m=[[None for i in range(len(matrice[0]))]for i in range(len(matrice))]
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            matrice_m[i][j]=scalaire*matrice[i][j]
            print(f"{matrice[i][j]} X {scalaire:.2f}  ",end="")
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

def multiplication(matrice1:list[int],matrice2:list[int])->list[int]:
            if len(matrice1[0]) != len(matrice2):
                raise ValueError

            matrice_multi=[[0 for i in range(len(matrice2[0]))]for i in range(len(matrice1))]
            for i in range(len(matrice1)):
                for j in range(len(matrice2[0])):
                    for k in range(len(matrice2)):
                        matrice_multi[i][j] += matrice1[i][k] * matrice2[k][j]
                        print(f"{matrice1[i][k]} X {matrice2[k][j]}  ",end="")
                    print()
            return matrice_multi

def Transpose(matrice:list[int])->list[int]:
    lignes=len(matrice)
    colones=len(matrice[0])
    matrice_Transpose=[[None for i in range(lignes)]for i in range(colones)]
    for i in range(lignes):
        for j in range(colones):
            matrice_Transpose[j][i]=matrice[i][j]
    return matrice_Transpose