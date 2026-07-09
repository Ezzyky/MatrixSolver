from matrice_io import *
from gauss import *
from menu_txtes import *
from operations import *
from utils import *
from analyse import *
import os

##########################
# hi there!
# if you are looking at this msg
# thank god, i will save your mental life
# you will ask "from what?"
# i am gonna save you from one of the stupidest and worst codes ever
# don't try to understand it only if YOU are crazy
# even after coming back to it days later i am still struggling right now
# thank you!
###########################
#la premire page 
home()
clear_avec_msg("Appuyez sur \"Entre\" bouton pour contune...")

#une liste pour l'option 25 
historique_list=[]
while True:
        #affichage de menu et input d option et clear
        os.system("cls" if os.name == "nt" else "clear")
        menu()
        try:
            option = int(input( "Choisissez une option : "))
        except ValueError:
            titre("Error!")
            clear_avec_msg("----> Option invalide.")
            continue
        os.system("cls" if os.name == "nt" else "clear") 

        #option 1 = Addition 
        if option==1:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")         
            matrice_pour_add=demander_matrice("B",1,matrice,"Addition")
            os.system("cls" if os.name == "nt" else "clear")
            lignes_B=len(matrice_pour_add)
            colonnes_B=len(matrice_pour_add[0])
            titre("Addition de matrices.")
            print("--> Matrice initiale A:")
            affichage(matrice)
            print("--> Matrice à ajouter B:")    
            affichage(matrice_pour_add)
            print("--> Calcul de la addition par le matrice B :")
            adition_matrice=addition(matrice,matrice_pour_add)
            print("--> Résultat de l'addition :")
            historique_list.append("Addition")
            affichage(adition_matrice)
            if all(all(x==0 for x in lignes)for lignes in adition_matrice ):
                titre("Note!")
                print("-----> La matrice est une matrice nulle!")
            sous_menu()
            options(historique_list,Addition_info,"Addition",("Matrice initiale",matrice),("Matrice à ajouter B",matrice_pour_add),("Résultat de l'addition",adition_matrice))

        #option 2 = Soustraction
        elif option==2:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            matrice_pour_oustraction=demander_matrice("B",1,matrice)
            os.system("cls" if os.name == "nt" else "clear")
            lignes_B=len(matrice_pour_oustraction)
            colonnes_B=len(matrice_pour_oustraction[0])
            titre("Soustraction de matrices")
            print("--> Matrice initiale A :")
            affichage(matrice)
            print("--> Matrice à soustraire B :")
            affichage(matrice_pour_oustraction)
            print("--> Calcul de la soustraction par le matrice B :")
            soustraction_matrice = souetraction(matrice, matrice_pour_oustraction)
            print("--> Résultat de la soustraction :")
            historique_list.append("Soustraction")
            affichage(soustraction_matrice)
            if all(all(x==0 for x in lignes)for lignes in soustraction_matrice ):
                titre("Note!")
                print("-----> La matrice est une matrice nulle!")
            sous_menu()
            options(historique_list,Soustraction_info,"Soustraction de matrices",("Matrice initiale",matrice),("Matrice à soustraire B",matrice_pour_oustraction),("Résultat de la soustraction",soustraction_matrice))

        #option 3 = Multiplication 
        elif option==3:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            matrice_pour_m=demander_matrice("B",2,matrice)
            os.system("cls" if os.name == "nt" else "clear") 
            titre("Multiplication")
            print("--> Matrice initiale A :")
            affichage(matrice)
            print("--> Matrice à multiplier B :")
            affichage(matrice_pour_m)
            print("--> Calcul de la Multiplication par le matrice B :")
            historique_list.append("Multiplication")
            matrice_multiple_par_Matrice=multiplication(matrice,matrice_pour_m,1)
            print("--> Résultat de la multiplication")
            affichage(matrice_multiple_par_Matrice)
            if all(all(x==0 for x in lignes)for lignes in matrice_multiple_par_Matrice ):
                titre("Note!")
                print("-----> La matrice est une matrice nulle!")
            #pour le  sous menu
            sous_menu()
            options(historique_list,Multiplication_info,"Multiplication",("Matrice initiale",matrice),("Matrice à multiplier B",matrice_pour_m),("Résultat de la multiplication",matrice_multiple_par_Matrice))

        #option 4 = Multiplication par scalaire
        elif option==4:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            titre("Multiplication par scalaire")
            try:
                scalaire=float(input("Veuillez entrer le scalaire à multiplier par la matrice: "))
            except ValueError:
                    titre("Error!")
                    print("---> Veuillez entrer un nombre valide !")
                    print()
                    clear_avec_msg()
                    continue
            historique_list.append("--> Multiplication par scalaire")
            print("--> Matrice initiale :")
            affichage(matrice)
            matrice_multipli_scalaire=multiplication_scalaire(matrice,scalaire)
            print("--> Matrice obtenue après multiplication par le scalaire :")
            affichage(matrice_multipli_scalaire)
            sous_menu()
            options(historique_list,Multiplication_par_scalaire_info,"Multiplication par scalaire",("Matrice initiale",matrice),("Multiplication par scalaire",scalaire),("Matrice obtenue après multiplication par le scalaire",matrice_multipli_scalaire))
        
        #option 5 = Transposée    
        elif option==5:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            titre("Transposée")
            print("--> Matrice initiale :")
            affichage(matrice)
            matrice_Transpose=Transpose(matrice)
            historique_list.append("Transposée")
            print("--> Résultat de la transposition :")
            print("Aᵀ",end="")
            affichage(matrice_Transpose)
            sous_menu()
            options(historique_list,Transpose_info,"Transposée",("Matrice initiale",matrice),("Résultat de la transposition",matrice_Transpose))
        #option 6= la puissance d'une matrice
        elif option==6:
            matrice=demander_matrice("A",3)
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            titre("la puissance d'une matrice")
            try:
                N_pour_la_puissance=int(input("Veuillez entrer l'exposant de la matrice :"))
            except ValueError:
                    titre("Error!")
                    print("----> Veuillez entrer un nombre valide !")
                    print()
                    clear_avec_msg()
                    continue
            print("--> Matrice initiale :")
            affichage(matrice)
            try:
                matrice_avec_puissance=puissance_matrice(matrice,N_pour_la_puissance)
            except ErrorNegative as i:
                 titre("Error!")
                 print(i)
                 clear_avec_msg()
                 continue
            print("--> Résultat de la puissance :")
            affichage(matrice_avec_puissance)
            historique_list.append("la puissance d'une matrice")
            sous_menu()
            options(historique_list,puissance_info,"la puissance d'une matrice",("Matrice initiale",matrice),("Résultat de la puissance",N_pour_la_puissance),("Résultat de l'addition",matrice_avec_puissance))

        #option 7 = reduction de gauss
        elif option==7:
            import copy
            matrice=demander_matrice()
            matrice_initiale=copy.deepcopy(matrice)
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            lignes=len(matrice)
            colonnes=len(matrice[0])
            titre("Réduction de Gauss")
            print("Matrice initiale :")
            affichage(matrice)
            print()
            if all(all(x==0 for x in lignes)for lignes in matrice ):
                titre("Note!")
                print("-----> La matrice est une matrice nulle!") 
                clear_avec_msg()
                continue

            try:
                Reduction_de_Gauss(matrice)
            except seule_ligne as e:
                titre("Note!")
                print(e)
                clear_avec_msg()
                continue
            #affichge de resulta fianle
            historique_list.append("reduction de gauss")
            print("--> Resulta finale:")
            affichage(matrice)
            sous_menu()
            options(historique_list,Reduction_Gauss_info,"reduction de gauss",("Matrice initiale",matrice_initiale),("reduction de gauss resulta finale",matrice))
        #option 11: déterminant 
        elif option==11:
            matrice=demander_matrice("A",3)
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            titre("déterminant")
            print("--> Matrice initiale :")
            affichage(matrice)
            print("--> Résultat de la déterminant :")
            print("det(A)=",(determinant(matrice)))
            historique_list.append("déterminant")
            sous_menu()
            options(historique_list,determinant_info,"déterminant",("Matrice initiale",matrice),("Résultat de la déterminant",determinant(matrice)))

        #option 15 : trace
        elif option==15:
            matrice=demander_matrice("A",3)
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            titre("Trace")
            print("--> Matrice initiale :")
            affichage(matrice)
            print("--> Résultat de la trace :")
            print("Tr(A)=",trace(matrice))
            historique_list.append("Trace")
            sous_menu()
            options(historique_list,Trace_info,"trace",("Matrice initiale",matrice),("Résultat de la trace",trace(matrice)))
        #option 16 : Inverse
        elif option==16:
            matrice=demander_matrice("A",3)
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            titre("Inverse")
            try:
                 inverse_de_matrice=inverse(matrice)
            except matricePASinverse as e:
                titre("NOTE!")
                print(e)
                clear_avec_msg()
                continue

            print("--> Matrice initiale :")
            affichage(matrice)
            formul_inverse()
            print("--> Résultat du calcul de l'inverse :")  
            affichage(inverse_de_matrice)    
            sous_menu()
            options(historique_list,invers_info(),"Inverse",("Matrice initiale",matrice),("Résultat du calcul de l'inverse",inverse(matrice)))
     
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