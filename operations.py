# Multiplie chaque élément d'une matrice par un scalaire.
def multiplication_scalaire(
    matrice: list[int], scalaire: float, flag: int = 0
) -> float:
    # La matrice résultat conserve les dimensions de la matrice d'origine.
    matrice_m = [[None for i in range(len(matrice[0]))] for i in range(len(matrice))]
    # Le mode détaillé affiche les calculs élémentaires sans modifier le résultat.
    if flag == 0:
        print(f"Calcul de la multiplication par le scalaire {scalaire:.1f} :")
        print()
    # Parcourt chaque coefficient afin de lui appliquer le même facteur.
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            matrice_m[i][j] = scalaire * matrice[i][j]
            if flag == 0:
                print(f"{matrice[i][j]} X {scalaire:.1f}  ", end="")
                print()
    return matrice_m


# Additionne deux matrices élément par élément.
def addition(matrice1: list[int], matrice2: list[int]) -> list[int]:
    # Le résultat a la même forme que les deux opérandes.
    matrice_add = [
        [None for i in range(len(matrice2[0]))] for i in range(len(matrice2))
    ]
    # Combine les coefficients occupant la même position dans les deux matrices.
    for i in range(len(matrice1)):
        for j in range(len(matrice2[0])):
            matrice_add[i][j] = matrice1[i][j] + matrice2[i][j]
            print(f"{matrice1[i][j]} + {matrice2[i][j]}  ", end="")
            print()
    return matrice_add


# Soustrait la seconde matrice de la première élément par élément.
def souetraction(matrice1: list[int], matrice2: list[int]) -> list[int]:
    # Prépare une matrice de même taille pour conserver chaque différence.
    matrice_souetraction = [
        [None for i in range(len(matrice2[0]))] for i in range(len(matrice2))
    ]
    # Compare les coefficients placés aux mêmes indices dans les deux matrices.
    for i in range(len(matrice1)):
        for j in range(len(matrice2[0])):
            matrice_souetraction[i][j] = matrice1[i][j] - matrice2[i][j]
            print()
            print(f"{matrice1[i][j]}-{matrice2[i][j]}  ", end="")
            print()
    return matrice_souetraction


# Calcule le produit matriciel de deux matrices compatibles.
def multiplication(
    matrice1: list[int], matrice2: list[int], flag: int = 0
) -> list[int]:
    # Initialise les sommes partielles de chaque coefficient du produit.
    matrice_multi = [[0 for i in range(len(matrice2[0]))] for i in range(len(matrice1))]
    # Associe chaque ligne de la première matrice à chaque colonne de la seconde.
    for i in range(len(matrice1)):
        for j in range(len(matrice2[0])):
            # Accumule les produits nécessaires à l'entrée courante du résultat.
            for k in range(len(matrice2)):
                matrice_multi[i][j] += matrice1[i][k] * matrice2[k][j]
                if flag == 1:
                    print(f"{matrice1[i][k]} X {matrice2[k][j]}")
    return matrice_multi


# Construit la transposée d'une matrice en échangeant lignes et colonnes.
def Transpose(matrice: list[int]) -> list[int]:
    lignes = len(matrice)
    colones = len(matrice[0])
    # La transposée inverse les dimensions lignes × colonnes.
    matrice_Transpose = [[None for i in range(lignes)] for i in range(colones)]
    # Inverse les indices de chaque coefficient pour échanger lignes et colonnes.
    for i in range(lignes):
        for j in range(colones):
            matrice_Transpose[j][i] = matrice[i][j]
    return matrice_Transpose


# Exception levée lorsqu'un exposant de matrice est négatif.
class ErrorNegative(Exception):
    pass


# Calcule une puissance entière non négative par multiplications successives.
def puissance_matrice(matrice: list[list[int]], N: int) -> list[list[int]]:
    # Refuse les exposants négatifs, non pris en charge par cette implémentation.
    if N < 0:
        raise ErrorNegative("----> La puissance doit être positive ou nulle.")
    if N == 0:
        taille = len(matrice)
        # La puissance zéro correspond à la matrice identité.
        return [[1 if i == j else 0 for j in range(taille)] for i in range(taille)]
    if N == 1:
        print()
        return matrice
    # Réutilise le résultat intermédiaire pour multiplier la matrice N - 1 fois.
    resulta = matrice
    # À partir de A, répète N - 1 multiplications pour obtenir A^N.
    for _ in range(N - 1):
        resulta = multiplication(resulta, matrice)
    return resulta
