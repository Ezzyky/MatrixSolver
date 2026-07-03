def trace(matrice:list[int])->int:
    if len(matrice)!=len(matrice[0]):
        raise ValueError
    t=0
    for i in range(len(matrice)):
        t+=matrice[i][i]
    return t
