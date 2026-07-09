from menu_txtes import *
from utils import clear_avec_msg
from colorama import *
init(autoreset=True)
#ajout un exception pour les errors
class MatrixSizeError(Exception):
    pass
class dimensions(Exception):
    pass
class nombreLIGNESmemeDEcolonnes(Exception):
    pass
class carree(Exception):
    pass

def prenant_matrice(nom:str="A",flag:int=0,matrice2:list[list[int]]=None,msg:str="soustraction")->list[int]:
    print(f"Saisissez la taille de la matrice {nom}:")
    
    lignes=int(input("Nombre de lignes : "))
    colonnes=int(input("Nombre de colonnes : "))
    if lignes<=0 or colonnes<=0:
       raise MatrixSizeError("----> Le nombre de lignes et de colonnes doit être strictement positif.")
    if flag==1:
        if len(matrice2)!=lignes or len(matrice2[0])!=colonnes:
            raise dimensions(f"""-----> {msg} impossible — dimensions incompatibles ({Fore.RED+str(len(matrice2))}x{Fore.RED+str(len(matrice2[0]))} ≠ {Fore.RED+str(lignes)}x{Fore.RED+str(colonnes)}{Style.RESET_ALL})""")
    if flag==2:
        if len(matrice2[0])!=lignes:
            raise nombreLIGNESmemeDEcolonnes("----> Multiplication impossible : le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la deuxième.")
    if flag==3:
        if lignes!=colonnes:
            raise carree("----> La matrice doit être carrée.")
    Matrice=[[None for i in range(colonnes)]for i in range (lignes)]
    print(f"\nSaisissez les éléments de la matrice ({Fore.GREEN+str(lignes)} × {Fore.GREEN+str(colonnes)}{Style.RESET_ALL}) :\n")
    for i in range(lignes):
        for j in range(colonnes):
            Matrice[i][j] = int(input(f"Élément de la ligne {i+1}, colonne {j+1} : "))
    return Matrice

#to exept the error out fo size tables
def demander_matrice(nom: str="A",falg:int=0,matrice:list[list[int]]=None,msg:str="soustraction")->None:
    
    while True:
        titre(f"Veuillez entrer la matrice initiale {nom}.")
        try:
             return prenant_matrice(nom,falg,matrice,msg)
        except ValueError:
            print()
            titre(Fore.RED+"Error!")
            print("----> Veuillez entrer un nombre valide.")
            clear_avec_msg()
        except MatrixSizeError as e:
            print()
            titre(Fore.RED+"Error!")
            print(e)
            clear_avec_msg()
        except dimensions as i:
            print()
            titre(Fore.RED+"Error!")
            print(i)
            clear_avec_msg()
        except nombreLIGNESmemeDEcolonnes as n:
            print()
            titre(Fore.RED+"Error!")
            print(n)
            clear_avec_msg()
        except carree as e:
            print()
            titre(Fore.RED+"Error!")
            print(e)
            clear_avec_msg()
        
def affichage(matrice:list[int])->None:
    lignes =len(matrice)
    print("\n")
    for i in range(lignes):
        if i==0:
            debut,fin="⎡", "⎤"
        elif i==lignes-1:
            debut,fin="⎣", "⎦"
        else:
            debut,fin="⎢", "⎥"
        print(debut, end=" ")
        for x in matrice[i]:
            print(f"{x:.1f}",end=" ")
        print(fin)
    print()
    

# i dont need it for now
def swap(matrice):
    lignes=len(matrice)
    colonnes=len(matrice[0])
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

def Operations_gauss_affichage(matrice:list[int],ligne_pivot:int,col_pivot:int)->None:
    lignes = len(matrice)
    colonnes = len(matrice[0])
    print("_________Opérations effectuées sur les lignes :_________")
    print()
    for j in range(ligne_pivot + 1, lignes):
        if matrice[j][col_pivot] != 0:
            a = matrice[j][col_pivot]
            p = matrice[ligne_pivot][col_pivot]
            if a<0:
                print(f"L{j+1} ← {p}L{j+1} + {a*(-1)}L{ligne_pivot+1}")
                print()
            else:
                print(f"L{j+1} ← {p}L{j+1} - {a}L{ligne_pivot+1}")
                print()
            for i in range(col_pivot, colonnes):
                matrice[j][i] = matrice[j][i] * p - matrice[ligne_pivot][i] * a