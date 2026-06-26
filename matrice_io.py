def prenant_matrice(nom="A"):
    print(f"Saisissez la taille de la matrice {nom}:")
    
    lignes=int(input("Nombre de lignes : "))
    colonnes=int(input("Nombre de colonnes : "))
    while lignes==0 or colonnes == 0:
        print("Erreur : le nombre de lignes et de colonnes doit être supérieur à 0.")
        lignes=int(input("Nombre de lignes : "))
        colonnes=int(input("Nombre de colonnes : "))
    Matrice=[[None for i in range(colonnes)]for i in range (lignes)]
    for i in range(lignes):
        for j in range (colonnes):
            Matrice[i][j]=int(input(f"M[{i+1}][{j+1}] = "))
    return Matrice

def affichage(matrice):
    lignes =len(matrice)
    for i in range(lignes):
        if i==0:
            debut,fin="⎡", "⎤"
        elif i==lignes-1:
            debut,fin="⎣", "⎦"
        else:
            debut,fin="⎢", "⎥"
        print(debut, end=" ")
        for x in matrice[i]:
            print(x,end=" ")
        print(fin)