# Importation des modules utilisés par l'application.
from matrice_io import *
from gauss import *
from menu_txtes import *
from operations import *
from utils import *
from analyse import *
from copy import *
import os

# Point d'entrée de l'interface console : coordonne la saisie, les calculs et leur affichage.
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

#La premire page 
# Initialise l'écran d'accueil de l'application.
os.system("cls" if os.name == "nt" else "clear")
home()
clear_avec_msg("Appuyez sur \"Entre\" bouton pour contune...")

#une liste pour l'option 25 
# Mémorise les opérations réalisées pendant la session pour l'option Historique.
historique_list=[]
# Boucle principale d'affichage et de traitement du menu.
while True:
        #affichage de menu et input d option et clear
        # Affiche le menu et récupère l'option choisie par l'utilisateur.
        os.system("cls" if os.name == "nt" else "clear")
        menu()
        try:
            option = int(input( "Choisissez une option : "))
        # Une saisie non entière laisse l'application active et ramène au menu.
        except ValueError:
            titre("Error!")
            clear_avec_msg("----> Option invalide.")
            continue
        os.system("cls" if os.name == "nt" else "clear") 

        #option 1 = Addition 
        if option==1:
            try:
                matrice=demander_matrice()
            except ValueError:
                continue
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
            try:
                matrice=demander_matrice()
            except ValueError:
                continue
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
            try:
                matrice=demander_matrice()
            except ValueError:
                continue
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
            try:
                matrice=demander_matrice()
            except ValueError:
                continue
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
            try:
                matrice=demander_matrice()
            except ValueError:
                continue
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
            try:
                matrice:list[list[float]]=demander_matrice("A",3)
            except ValueError:
                continue
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
            options(historique_list,puissance_info,"la puissance d'une matrice",("Matrice initiale",matrice),("Résultat de la puissance",N_pour_la_puissance))

        #option 7 = reduction de gauss
        elif option == 7:
            try:
                matrice=demander_matrice()
            except ValueError:
                continue
            # La réduction modifie la matrice en place ; cette copie conserve l'état initial.
            matrice_initiale=deepcopy(matrice)
            lignes=len(matrice)
            colonnes=len(matrice[0])
            titre("Réduction de Gauss")
            print("--> Matrice initiale :")
            affichage(matrice)
            # Une matrice nulle ne fournit aucun pivot exploitable pour l'élimination.
            if all(all(x==0 for x in lignes)for lignes in matrice ):
                titre("Note!")
                print("-----> La matrice est une matrice nulle!") 
                clear_avec_msg()
                continue

            try:
                Reduction_de_Gauss(matrice,0)
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
        #option 10 : rang
        elif option == 10:
            try:
                matrice=demander_matrice()
            except ValueError:
                continue
            matrice_initiale=deepcopy(matrice)
            try:
                rg=rang(matrice)
            except seule_ligne as e:
                titre("Note!")
                print(e)
                clear_avec_msg()
                continue
            titre("Rang")
            print()
            print("--> Matrice initiale :")
            affichage(matrice_initiale)
            print("--> Matrice reduite :")
            affichage(matrice)
            print("--> Résultat du calcul du rang :")
            print(f"\nrg(A) ={rg}")
            historique_list.append("Rang")
            sous_menu()
            options(historique_list,rang_info,rang,"Rang",("Matrice initiale :",matrice_initiale),("Matrice reduite : :",matrice),("Résultat du calcul du rang\nrg(A) =",rang(matrice)))

            #option 11: déterminant 
        elif option == 11:
            # Propose les différentes opérations relatives au déterminant.
            sous_detiminent()
            try:
                sous_option = int( input("Choisissez une option : "))
            except ValueError:
                clear_avec_msg("Option invalide.")
                continue
            os.system("cls")
            try:
                matrice=demander_matrice("A",3)
            except ValueError:
                continue
            det_a=determinant(matrice)
            if sous_option==1:
                titre("déterminant det(A)")
                print("--> Matrice initiale :")
                affichage(matrice)
                print("--> Résultat de la déterminant de A :")
                print("det(A) = ",(det_a))
                historique_list.append("déterminant det(A)")
                sous_menu()
                options(historique_list,determinant_info,"déterminant",("Matrice initiale",matrice),("Résultat de la déterminant de A :\ndet(A)=",det_a))
            elif sous_option==2:
                titre("déterminant det(Aᵀ)")
                print("--> Matrice initiale :")
                affichage(matrice)
                print("--> Résultat de la déterminant de Aᵀ:")
                print("det(Aᵀ) = ",(det_a))
                historique_list.append("Calculer det(Aᵀ)")
                sous_menu()
                options(historique_list,determinant_info,"déterminant",("Matrice initiale",matrice),("Résultat de la déterminant de Aᵀ:\ndet(Aᵀ) = ",det_a))
            elif sous_option==3:
                matrice_b=demander_matrice("A",4,matrice)
                titre("déterminant det(AB)")
                print("--> Les matrices initiale :")
                affichage(matrice)
                affichage(matrice_b)
                print("det(A) = " ,(det_a),end="")
                print(", det(B) = ",(determinant(matrice_b)))
                print()
                print("--> Resulta finale:")
                # Utilise la propriété det(AB) = det(A) × det(B).
                axb=det_a*determinant(matrice_b)
                print(f"det(AB)={axb}")
                historique_list.append("Calculer det(AB)")
                sous_menu()
                options(historique_list,determinant_info,"déterminant",("Matrice initiale A",(matrice)),("Matrice initiale B",(matrice_b)),("det(A) = ",det_a),("det(B) = ",determinant(matrice_b)),("det(AB) = ",axb))
            elif sous_option==4:
                titre("Calculer det(kA)")
                try:
                    scalaire=float(input("Veuillez entrer le scalaire à multiplier par la matrice: "))
                except ValueError:
                        titre("Error!")
                        print("---> Veuillez entrer un nombre valide !")
                        print()
                        clear_avec_msg()
                        continue
                print("La matrice initiale :")
                affichage(matrice)
                print(f"--> det(A) ={det_a:.1f}, n = {len(matrice)}, K ={scalaire:.1f}.")
                detKA()
                print("--> Resulta finale:")
                KA:float=(scalaire**len(matrice))*det_a
                print(f"det({scalaire:.0f}A) = {KA:.2f}")
                historique_list.append("Calculer det(kA)")
                sous_menu()
                options(historique_list,determinant_info,"déterminant det(kA)",("Matrice initiale A",(matrice)),("n = ",len(matrice)),("det(A) = ",det_a),("K = ",scalaire),("det(KB) = ",KA))
            elif sous_option==5:
                titre("Calculer det(A⁻¹)")
                if det_a==0:
                    titre("Note!")
                    print("--> Elle doit être inversible, c'est-à-dire det(A) ≠ 0.")
                    clear_avec_msg()
                    continue
                print("La matrice initiale :")
                affichage(matrice)
                print("--> Resulta finale:")
                print(f"det(A⁻¹) = {1/det_a:.3f}")
                historique_list.append("Calculer det(A⁻¹)")
                sous_menu()
                options(historique_list,determinant_info,"déterminant",("Matrice initiale A",(matrice)),("Resulta finale\ndet(A⁻¹)",1/det_a))
            elif sous_option==0:
                os.system("cls" if os.name == "nt" else "clear")
            else:
             titre(titre(f"L'option {sous_option} n'existe pas."))
             clear_avec_msg()
        #option: Vérifier inversible
        elif option==12:
            try:
                matrice=demander_matrice("A",3)
            except ValueError:
                continue
            titre("Vérifier inversible")
            print("--> Matrice initiale :")
            affichage(matrice)
            det=determinant(matrice)
            # Une matrice carrée est inversible lorsque son déterminant est non nul.
            if determinant(matrice)!=0:
                print(" Résultat :")
                print()
                print(f"On a det(A) = {det}.")
                print("Donc, la matrice est inversible car det(A) ≠ 0.")
                historique_list.append("Vérifier inversible")
                sous_menu()
                options(historique_list,verifier_inversible_info,"Vérifier inversible",("Matrice initiale",matrice),("Résultat\nOn a det(A) = ", det),("Donc, la matrice est inversible car det(A) ≠ ",0))
            else:
                print(" Résultat :")
                print()
                print(f"On a det(A) = {det}.")
                print("Donc, la matrice n'est pas inversible car det(A) = 0.")
                historique_list.append("Vérifier inversible")
                sous_menu()
                options(historique_list,verifier_inversible_info,"Vérifier inversible",("Matrice initiale",matrice),("Résultat\nOn a det(A) = ",det),("Donc, la matrice n'est pas inversible car det(A) = ",0))
        # option : Vérifier symétrique Trace
        elif option==13:
            try:
                matrice=demander_matrice("A",3)
            except ValueError:
                continue
            titre("Vérifier symétrique Trace")
            print("--> Matrice initiale :")
            affichage(matrice)
            det=determinant(matrice)
            print("--> Résultat :")
            print()
            # Compare la matrice à sa transposée pour déterminer sa symétrie.
            if Transpose(matrice)==matrice:
                print("--> On a Aᵀ= :")
                affichage(Transpose(matrice))
                print("--> Donc, La matrice est symétrique car Aᵀ = A.")
                historique_list.append("Vérifier inversible")
                sous_menu()
                options(historique_list,verifier_symetrique_info,"Vérifier symétrique Trace",("Matrice initiale",matrice),("--> On a Aᵀ= :",Transpose(matrice)),("Donc, La matrice est symétrique car Aᵀ = A.",None))
            else:
                print("--> On a Aᵀ= :")
                affichage(Transpose(matrice))
                print("--> Donc, La matrice n'est pas symétrique car Aᵀ ≠ A.")
                historique_list.append("Vérifier inversible")
                sous_menu()
                options(historique_list,verifier_symetrique_info,"Vérifier symétrique Trace",("Matrice initiale",matrice),("--> On a Aᵀ= :",Transpose(matrice)),("Donc, La matrice est symétrique car Aᵀ = A.",None))
        elif option == 14:
            try:
                matrice=demander_matrice("A",3)
            except ValueError:
                continue
            titre("diagonale")
            print("--> Matrice initiale :")
            affichage(matrice)
            print("--> Résultat :")
            print()
            historique_list.append("Vérifier diagonaleInverse")
            if diagonale(matrice) is True:
                print("La matrice est diagonale.")
                print("Donc, elle est inversible.")
                sous_menu()
                options(historique_list,diagonale_info,"diagonaleInverse",("Matrice initiale",matrice),("Donc, La matrice est diagonaleInverse\nDonc, elle est inversible.",None))
            else:
                print("La matrice n'est pas diagonale.")
                print("Elle ne peut donc pas être considérée comme une matrice diagonale inversible.")
                sous_menu()
                options(historique_list,diagonale_info,"diagonaleInverse",("Matrice initiale",matrice),("La matrice n'est pas diagonale.\nElle ne peut donc pas être considérée comme une matrice diagonale inversible",None))
        #option 15 : trace
        elif option==15:
            try:
                matrice=demander_matrice("A",3)
            except ValueError:
                continue
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
            try:
                matrice=demander_matrice("A",3)
            except ValueError:
                continue
            titre("Inverse")
            # Une matrice non inversible est signalée par une exception pour préserver le menu.
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
            options(historique_list,invers_info,"Inverse",("Matrice initiale",matrice),("Résultat du calcul de l'inverse",inverse(matrice)))
     
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
        #home
        # Réaffiche l'accueil sans quitter la boucle principale.
        elif option==25:
            home()
            clear_avec_msg("Appuyez sur \"Entre\" bouton pour contune...")
            continue

        #option 0 = Quitter
        elif option==0:
            Quitter()
        else:
            titre(f"L'option {option} n'existe pas.")
            clear_avec_msg()