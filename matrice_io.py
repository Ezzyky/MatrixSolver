# Fonctions de saisie, validation et affichage des matrices.
from menu_txtes import *
from utils import clear_avec_msg

# Exceptions associées à la validation des dimensions des matrices.
#ajout un exception pour les errors
class MatrixSizeError(Exception):
    pass
class dimensions(Exception):
    pass
class nombreLIGNESmemeDEcolonnes(Exception):
    pass
class carree(Exception):
    pass
class carrees_ordre(Exception):
    pass
# Saisit une matrice et vérifie les contraintes liées à l'opération demandée.
def prenant_matrice(nom:str="A",flag:int=0,matrice2:list[list[float]]=None,msg:str="soustraction")->list[list[float]]:
    print(f"Saisissez la taille de la matrice {nom}:")
    lignes=int(input("Nombre de lignes : "))
    colonnes=int(input("Nombre de colonnes : "))
    # Les dimensions doivent être strictement positives avant toute allocation.
    # Le drapeau sélectionne la contrainte de compatibilité liée à l'opération.
    if lignes<=0 or colonnes<=0:
       raise MatrixSizeError("----> Le nombre de lignes et de colonnes doit être strictement positif.")
    # L'addition et la soustraction exigent deux matrices de même dimension.
    elif flag==1:
        if len(matrice2)!=lignes or len(matrice2[0])!=colonnes:
            raise dimensions(f"""-----> {msg} impossible — dimensions incompatibles ({(len(matrice2))}x{(len(matrice2[0]))} ≠ {(lignes)}x{(colonnes)})""")
    # Le produit matriciel impose colonnes(A) = lignes(B).
    elif flag==2:
        if len(matrice2[0])!=lignes:
            raise nombreLIGNESmemeDEcolonnes("----> Multiplication impossible : le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la deuxième.")
    # Certaines opérations, comme le déterminant, exigent une matrice carrée.
    elif flag==3:
        if lignes!=colonnes:
            raise carree("----> La matrice doit être carrée.")
    # Cette variante vérifie deux matrices carrées de même ordre.
    elif flag == 4:
        if (lignes!=len(matrice2) and colonnes!=len(matrice2[0])) or lignes!=colonnes:
            raise carrees_ordre(f"----> Les matrices A et B doivent être carrées et de même ordre ({(len(matrice2))}x{(len(matrice2[0]))} ≠ {(lignes)}x{(colonnes)}).")
    # Préalloue la grille afin de renseigner les coefficients ligne par ligne.
    Matrice=[[None for i in range(colonnes)]for i in range (lignes)]
    print(f"\nSaisissez les éléments de la matrice ({(lignes)} × {(colonnes)}) :\n")
    for i in range(lignes):
        for j in range(colonnes):
            Matrice[i][j] = float(input(f"Élément de la ligne {i+1}, colonne {j+1} : "))
    clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
    return Matrice

# Gère les erreurs de saisie jusqu'à l'obtention d'une matrice valide.
# exept the error 
def demander_matrice(nom: str="A",falg:int=0,matrice:list[list[float]]=None,msg:str="soustraction")->None:
    
    while True:
        titre(f"Veuillez entrer la matrice initiale {nom}.")
        try:
             return prenant_matrice(nom,falg,matrice,msg)
        except ValueError:
            print()
            titre("Error!")
            print("----> Veuillez entrer un nombre valide.")
            clear_avec_msg()
        except MatrixSizeError as e:
            print()
            titre("Error!")
            print(e)
            clear_avec_msg()
        except dimensions as i:
            print()
            titre("Error!")
            print(i)
            clear_avec_msg()
        except nombreLIGNESmemeDEcolonnes as n:
            print()
            titre("Error!")
            print(n)
            clear_avec_msg()
        except carree as e:
            print()
            titre("Error!")
            print(e)
            clear_avec_msg()
        except carrees_ordre as e:
            print()
            titre("Error!")
            print(e)
            clear_avec_msg()
        
# Affiche une matrice avec des bordures adaptées à ses lignes.
def affichage(matrice:list[int])->None:
    lignes =len(matrice)
    print("\n")
    for i in range(lignes):
        # Adapte les délimiteurs à la première, aux lignes centrales et à la dernière ligne.
        if i==0:
            debut,fin="⎡ ", " ⎤"
        elif i==lignes-1:
            debut,fin="⎣ ", " ⎦"
        else:
            debut,fin="⎢ ", " ⎥"
        print(debut, end=" ")
        # Chaque élément est affiché avec une précision décimale uniforme.
        for x in matrice[i]:
            print(f" {x:.1f} ",end=" ")
        print(fin)
    print()
    

# Échange la première ligne avec une ligne dont le premier élément est non nul.
# i dont need it for now
def swap(matrice):
    lignes=len(matrice)
    colonnes=len(matrice[0])
    # Recherche un pivot non nul dans la première colonne avant la permutation.
    if matrice[0][0]==0:
        for i in range(lignes):
            if matrice[i][0]!=0:
                index=i
                break
        for i in range(colonnes):
            temp=matrice[0][i]
            matrice[0][i]=matrice[index][i]
            matrice[index][i]=temp
        print("_________Opérations effectuées sur les lignes :_________")
        print()
        print(f"L1 ​↔ L​{index+1}")
    return matrice

# Applique et affiche les opérations d'élimination sous un pivot de Gauss.
def Operations_gauss_affichage(matrice:list[int],ligne_pivot:int,col_pivot:int,flag:int=0)->None:
    lignes = len(matrice)
    colonnes = len(matrice[0])
    if flag==0:
        print("_________Opérations effectuées sur les lignes :_________")
        print()
    for j in range(ligne_pivot + 1, lignes):
        if matrice[j][col_pivot] != 0:
            a = matrice[j][col_pivot]
            p = matrice[ligne_pivot][col_pivot]
            if flag==0:
                if a<0:
                    print(f"L{j+1} ← {p}L{j+1} + {a*(-1)}L{ligne_pivot+1}")
                    print()
                else:
                    print(f"L{j+1} ← {p}L{j+1} - {a}L{ligne_pivot+1}")
                    print()
            # Combine les lignes sans division pour annuler le coefficient sous le pivot.
            for i in range(col_pivot, colonnes):
                matrice[j][i] = matrice[j][i] * p - matrice[ligne_pivot][i] * a
