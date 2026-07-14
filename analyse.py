# Calcule la somme des éléments de la diagonale principale.
def trace(matrice: list[int]) -> int:
    # La trace n'est définie ici que pour une matrice carrée.
    if len(matrice) != len(matrice[0]):
        raise ValueError
    # Accumule les termes de la diagonale principale pour former la trace.
    t = 0
    for i in range(len(matrice)):
        t += matrice[i][i]
    return t


# Calcule récursivement le déterminant d'une matrice carrée.
def determinant(matrice: list[list[int]]) -> float:
    colonne = len(matrice[0])
    lignes = len(matrice)
    # Cas de base traités directement avant le développement récursif.
    if colonne == 1 and lignes == 1:
        return matrice[0][0]
    elif colonne == 2 and lignes == 2:
        return (matrice[0][0] * matrice[1][1]) - (matrice[0][1] * matrice[1][0])
    # Applique la règle de Sarrus pour une matrice 3 × 3.
    elif colonne == 3 and lignes == 3:
        aei = matrice[0][0] * matrice[1][1] * matrice[2][2]
        bfg = matrice[0][1] * matrice[1][2] * matrice[2][0]
        cdh = matrice[0][2] * matrice[1][0] * matrice[2][1]
        ceg = matrice[0][2] * matrice[1][1] * matrice[2][0]
        bdi = matrice[0][1] * matrice[1][0] * matrice[2][2]
        afh = matrice[0][0] * matrice[1][2] * matrice[2][1]
        return aei + bfg + cdh - ceg - bdi - afh
    else:
        # Développe le déterminant suivant la première ligne pour les ordres supérieurs.
        i = 0
        s = 0
        # Additionne les cofacteurs associés aux éléments de la première ligne.
        for j in range(colonne):
            # Construit le mineur M₀ⱼ en retirant la première ligne et la colonne j.
            sous_matrice = [
                [matrice[r][c] for c in range(colonne) if c != j]
                for r in range(1, lignes)
            ]
            s += ((-1) ** (i + j)) * matrice[i][j] * determinant(sous_matrice)
        return s


# Exception levée lorsqu'une matrice n'admet pas d'inverse.
class matricePASinverse(Exception):
    pass


# Calcule l'inverse à partir de la comatrice et du déterminant.
def inverse(matrice) -> float:
    # Un déterminant nul interdit l'existence de l'inverse.
    if determinant(matrice) == 0:
        raise matricePASinverse(
            "La matrice n'est pas inversible, car son déterminant est nul (det(A) = 0)."
        )
    from operations import Transpose, multiplication_scalaire

    colonnes = len(matrice[0])
    lignes = len(matrice)
    # Réserve l'espace nécessaire aux cofacteurs de la matrice.
    comatrice = [[None for _ in range(colonnes)] for _ in range(lignes)]
    # Construit la matrice des cofacteurs à partir des mineurs.
    for i in range(lignes):
        for j in range(colonnes):
            sous_matrice = [
                [matrice[r][c] for c in range(colonnes) if c != j]
                for r in range(lignes)
                if r != i
            ]
            comatrice[i][j] = ((-1) ** (i + j)) * determinant(sous_matrice)
    # La transposée de la comatrice forme la matrice adjointe.
    co_matrice_transpose = Transpose(comatrice)
    # Multiplie l'adjointe par l'inverse du déterminant pour obtenir l'inverse.
    det_matrice = 1 / determinant(matrice)
    matrice_inverse = multiplication_scalaire(co_matrice_transpose, det_matrice, 1)
    return matrice_inverse


def diagonale(matrice: list[list[int]]) -> bool:
    colones = len(matrice[0])
    lignes = len(matrice)
    for i in range(lignes):
        for j in range(colones):
            if i != j and matrice[i][j] != 0:
                return False
    return True
