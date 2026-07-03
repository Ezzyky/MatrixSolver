from matrice_io import *
from gauss import *
from menu_txtes import *
from operations import *
from utils import *
from analyse import *
import os

#la premire page 
home()
clear_avec_msg()

#une liste pour l'option 25 
historique_list=[]
while True:
    
        #affichage de menu et input d option et clear
        os.system("cls" if os.name == "nt" else "clear")
        menu()
        try:
            option = int(input("Choisissez une option : "))
        except ValueError:
            clear_avec_msg("----> Option invalide.")
            continue
        os.system("cls" if os.name == "nt" else "clear") 

        #option 1 = Addition 
        if option==1:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")         
            matrice_pour_add=demander_matrice("B")
            os.system("cls" if os.name == "nt" else "clear")
            lignes_B=len(matrice_pour_add)
            colonnes_B=len(matrice_pour_add[0])
            if len(matrice)!=lignes_B or len(matrice[0])!=colonnes_B:
                print("Addition impossible : dimensions incompatibles.")
                clear_avec_msg()
                continue
            titre("Addition de matrices.")
            print("--> Matrice initiale A:")
            print()
            affichage(matrice)
            print()
            print("--> Matrice à ajouter B:")    
            print()
            affichage(matrice_pour_add)
            print()
            print("--> Calcul de la addition par le matrice B :")
            adition_matrice=addition(matrice,matrice_pour_add)
            print()
            print("--> Résultat de l'addition :")
            print()
            historique_list.append("Addition")
            affichage(adition_matrice)
            if all(all(x==0 for x in lignes)for lignes in adition_matrice ):
                print("-----> La matrice est une matrice nulle!")
            sous_menu()
            options(historique_list,"Addition",("Matrice initiale",matrice),("Matrice à ajouter B",matrice_pour_add),("Résultat de l'addition",adition_matrice))

        #option 2 = Soustraction
        elif option==2:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            matrice_pour_sost=demander_matrice(nom="B")

            os.system("cls" if os.name == "nt" else "clear")
            lignes_B=len(matrice_pour_sost)
            colonnes_B=len(matrice_pour_sost[0])
            if len(matrice)!=lignes_B or len(matrice[0])!=colonnes_B:
                print("-----> Soustraction impossible : dimensions incompatibles.")
                clear_avec_msg()
                continue
            titre("Soustraction de matrices")
            print("--> Matrice initiale A :")
            print()
            affichage(matrice)
            print()
            print("--> Matrice à soustraire B :")
            affichage(matrice_pour_sost)
            print()
            print("--> Calcul de la soustraction par le matrice B :")
            soustraction_matrice = souetraction(matrice, matrice_pour_sost)
            print()
            print("--> Résultat de la soustraction :")
            print()
            historique_list.append("Soustraction")
            affichage(soustraction_matrice)
            if all(all(x==0 for x in lignes)for lignes in soustraction_matrice ):
                print("-----> La matrice est une matrice nulle!")
            sous_menu()
            options(historique_list,"Soustraction de matrices",("Matrice initiale",matrice),("Matrice à soustraire B",matrice_pour_sost),("Résultat de la soustraction",soustraction_matrice))

        #option 3 = Multiplication 
        elif option==3:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            matrice_pour_m=demander_matrice("B")
            os.system("cls" if os.name == "nt" else "clear") 
            titre("Multiplication")

            print("--> Matrice initiale A :")
            print()
            affichage(matrice)
            print()
            print("--> Matrice à multiplier B :")
            print()
            affichage(matrice_pour_m)
            print()
            print("--> Calcul de la Multiplication par le matrice B :")
            print()
            try:
                matrice_multiple_par_Matrice=multiplication(matrice,matrice_pour_m,1)
            except ValueError:
                 print("----> Multiplication impossible : le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la deuxième.")
                 print()
                 clear_avec_msg()
                 continue
            historique_list.append("Multiplication")

            print("--> Résultat de la multiplication")
            print()
            affichage(matrice_multiple_par_Matrice)
            print()
            if all(all(x==0 for x in lignes)for lignes in matrice_multiple_par_Matrice ):
                print("-----> La matrice est une matrice nulle!")
            #pour le  sous menu
            sous_menu()
            options(historique_list,"Multiplication",("Matrice initiale",matrice),("Matrice à multiplier B",matrice_pour_m),("Résultat de la multiplication",matrice_multiple_par_Matrice))

        #option 4 = Multiplication par scalaire
        elif option==4:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            titre("Multiplication par scalaire")
            try:
                scalaire=float(input("Veuillez entrer le scalaire à multiplier par la matrice: "))
            except ValueError:
                    print("Veuillez entrer un nombre valide !")
                    print()
                    clear_avec_msg()
                    continue
            historique_list.append("Multiplication par scalaire")
            print("Matrice initiale :")
            print()
            affichage(matrice)
            print()
            matrice_multipli_scalaire=multiplication_scalaire(matrice,scalaire)
            print("Matrice obtenue après multiplication par le scalaire :")
            print()
            affichage(matrice_multipli_scalaire)
            sous_menu()
            options(historique_list,"Multiplication par scalaire",("Matrice initiale :",matrice),("Multiplication par scalaire :",scalaire),("Matrice obtenue après multiplication par le scalaire :",matrice_multipli_scalaire))
        
        #option 5 = Transposée    
        elif option==5:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            titre("Transposée")
            print("--> Matrice initiale :")
            print()
            affichage(matrice)
            matrice_Transpose=Transpose(matrice)
            historique_list.append("Transposée")
            print("--> Résultat de la transposition :")
            print()
            affichage(matrice_Transpose)
            print()
            sous_menu()
            options(historique_list,"Transposée",("Matrice initiale",matrice),("Résultat de la transposition",matrice_Transpose))

        #option 6= la puissance d'une matrice
        elif option==6:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            titre("la puissance d'une matrice")
            try:
                N_pour_la_puissance=int(input("Veuillez entrer l'exposant de la matrice :"))
            except ValueError:
                    print("----> Veuillez entrer un nombre valide !")
                    print()
                    clear_avec_msg()
                    continue
            print("--> Matrice initiale :")
            print()
            affichage(matrice)
            try:
                matrice_avec_puissance=puissance_matrice(matrice,N_pour_la_puissance)
            except ValueError as e:
                 print(e)
                 clear_avec_msg()
                 continue
            except ErrorNegative as i:
                 print(i)
                 clear_avec_msg()
                 continue
            print("--> Résultat de la puissance :")
            print()
            affichage(matrice_avec_puissance)
            print()
            historique_list.append("la puissance d'une matrice")
            sous_menu()
            options(historique_list,"la puissance d'une matrice",("Matrice initiale :",matrice),("Résultat de la puissance :",N_pour_la_puissance),("Résultat de l'addition",matrice_avec_puissance))

        #option 7 = reduction de gauss
        elif option==7:
            import copy

            matrice=demander_matrice()
            matrice_initiale=copy.deepcopy(matrice)
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            lignes=len(matrice)
            colonnes=len(matrice[0])
            titre("Réduction de Gauss")
            if all(all(x==0 for x in lignes)for lignes in matrice ):
                    print("-----> La matrice est une matrice nulle!") 
                    clear_avec_msg()
                    continue
            print("Matrice initiale :")
            print()
            affichage(matrice)
            # Permutation des lignes L1 et la première ligne dont le premier élément est non nul
            index=0
            if lignes>=2:   
                for pivot in range(min(lignes, colonnes)):
                    if matrice[pivot][pivot] == 0:
                        for i in range(pivot + 1, lignes):
                            if matrice[i][pivot] != 0:
                                matrice[pivot], matrice[i] = matrice[i], matrice[pivot]
                                print(f"\nL{pivot+1} ↔ L{i+1}")
                                affichage(matrice)
                                break
                    elimination_gauss(matrice, pivot)
                    if pivot < min(lignes, colonnes) - 1:
                        affichage(matrice)
                        print()
            else:
                print()
                print("----> La matrice contient une seule ligne. Aucune élimination n'est nécessaire.")
                clear_avec_msg()
                continue
            #affichge de resulta fianle
            historique_list.append("reduction de gauss")
            print("--> Resulta finale:")
            print()
            affichage(matrice)
            print()
            sous_menu()
            options(historique_list,"reduction de gauss",("Matrice initiale",matrice_initiale),("reduction de gauss resulta finale:",matrice))
        
        #option 13 : trace
        elif option==13:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            try:
                trace(matrice)
            except ValueError:
                print("----> La matrice doit être carrée.")
                clear_avec_msg()
                continue
            titre("Trace")
            historique_list.append("Trace")
            print("--> Matrice initiale :")
            print()
            affichage(matrice)
            print()
            print("--> Résultat de la trace :")
            print("Tr(A)=",trace(matrice))
            sous_menu()
            options(historique_list,"trace",("Matrice initiale",matrice),("Résultat de la trace :",trace(matrice)))

        
        #option 23 : historique
        elif option == 23:
            titre("Historique")
            historique(historique_list)
            clear_avec_msg()

        #infos
        elif option==24:
             titre("INFOS")
             infos()
             clear_avec_msg()
        
        #option 0 = Quitter
        elif option==0:
            Quitter()

        else:
             titre("pas de option!")
             clear_avec_msg()