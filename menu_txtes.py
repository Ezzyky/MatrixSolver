# Fonctions d'affichage des menus, messages et aides de l'application.
from time import strftime,localtime

# Date affichée dans le sous-menu de sauvegarde.
time=strftime("%d-%m-%Y", localtime())
# Affiche le menu principal des opérations disponibles.

def menu()->None:
    # Présente les commandes, regroupées par domaine, dans une seule vue.
    print("""
                =========================================================
                              APPLICATION D'ALGÈBRE LINÉAIRE
                =========================================================

[A] Opérations sur les matrices                   [B] Réduction et résolution
    [1]. Addition                                     [7]. Réduction de Gauss
    [2]. Soustraction                                 [8]. Méthode de Gauss-Jordan
    [3]. Multiplication                               [9]. Résolution système linéaire
    [4]. Multiplication par scalaire                  [10]. Rang
    [5]. Transposée AT
    [6]. la puissance d'une matrice



[C] Propriétés et analyse                         [D] Algèbre linéaire avancée
    [11]. Déterminant                                 [17]. Valeurs propres
    [12]. Vérifier inversible                         [18]. Vecteurs propres
    [13]. Vérifier symétrique Trace                   [19]. Noyau Ker(A)
    [14]. Vérifier diagonaleInverse                   [20]. Image Im(A)
    [15]. Trace                                       [21]. Décomposition LU
    [16]. Inverse                                     [22]. SVD


[E] Outils
    [23]. historique             [24]. Infos           [25]. Home

                                 [0]. Quitter
                                                                                           
""")

# Affiche la page d'accueil et la présentation de l'application.
def home()->None:
     # Affiche la bannière et les consignes avant l'accès aux fonctionnalités.
     print("""
           
                ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗
                ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝
                ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝
                ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗
                ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗
                ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
                ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗
                ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗
                ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝
                ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗
                ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║
                ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝

        Ce programme permet d'effectuer plusieurs opérations sur les matrices
        et les systèmes linéaires.

        Veuillez d'abord choisir l'opération souhaitée dans le menu suivant,
        puis saisir la matrice correspondante.
    
            ========================================================== 
                                  -> REMARQUE <-
           
        Ce programme accepte les matrices à coefficients entiers ainsi qu'à
        coefficients réels (float).
            ==========================================================
    """)
# Affiche les informations générales sur le projet.
def infos()->None:
    print(f"""
Description :
Ce programme a été développé en Python dans le cadre d'un projet
d'algèbre linéaire. Il permet d'effectuer diverses opérations sur
les matrices ainsi que la résolution de systèmes linéaires.


Informations :
Date de création : 24 juin 2026
Version          : 1.0
Langage          : Python

Développeur :
Nom              : Abdellah Ezzyky
E-mail           : Abdellahezzyky@gmail.com
GitHub           : https://github.com/EZZYKY
LinkedIn         : https://www.linkedin.com/in/abdellah-ezzyky-92b09a326

==============================================================

""")
# Affiche un titre centré et encadré.
def titre(txte:str)->None:
    print()
    # Une largeur fixe maintient l'alignement des titres dans le terminal.
    print("="*60)
    print(txte.center(60))
    print("="*60)
    print("\n")

# Affiche les actions disponibles après une opération.
def sous_menu()->None:
    # Insère la date du jour dans le nom de fichier proposé à l'utilisateur.
    print(f"""
          
========================================================== 
    [1]. Sauvegarder dans "{time}.txt"   
    [2]. Historique                           [0]. Retour 
    [3]. Explications        
==========================================================  """)

# Affiche le sous-menu des propriétés du déterminant.
def sous_detiminent()->None:
    print("""
==========================================================
          CALCUL DES PROPRIÉTÉS DU DÉTERMINANT
==========================================================
          
À partir de cette matrice, le programme appliquera
la propriété choisie et affichera le déterminant obtenu.
          

 [1]. Calculer det(A)          [4]. Calculer det(kA)
                                
 [2]. Calculer det(Aᵀ)         [5]. Calculer det(A⁻¹)
               
 [3]. Calculer det(AB)         [0]. Retour
         

==========================================================
""")
# --- Aides pédagogiques sur les propriétés et opérations matricielles ---
# Présente le critère permettant de vérifier l'inversibilité.
def verifier_inversible_info()->None:
    print("""
==========================================================
           VÉRIFICATION DE L'INVERSIBILITÉ
==========================================================

Une matrice est inversible si et seulement si son
déterminant est différent de zéro.

Conditions :
• La matrice doit être carrée (même nombre de lignes
  et de colonnes).
• det(A) ≠ 0

Formule :

            det(A) ≠ 0

Résultat :

• Si det(A) ≠ 0 :
  → La matrice est inversible.

• Si det(A) = 0 :
  → La matrice n'est pas inversible.
""")
# Explique la notion de matrice inversible.
def inversible_info()->None:
    print("""
==========================================================
         VÉRIFIER SI UNE MATRICE EST INVERSIBLE
==========================================================

Une matrice est dite inversible si elle possède une matrice
inverse.

Conditions :
• La matrice doit être carrée (même nombre de lignes et de
  colonnes).
• Son déterminant doit être différent de zéro.

Critère :

           det(A) ≠ 0  ⇒  A est inversible
           det(A) = 0  ⇒  A n'est pas inversible

Exemple 1 :

      ⎡1  2⎤
A =   ⎣3  4⎦

det(A) = (1 × 4) − (2 × 3)
        = 4 − 6
        = −2

Comme det(A) ≠ 0, la matrice est inversible.

Exemple 2 :

      ⎡1  2⎤
A =   ⎣2  4⎦

det(A) = (1 × 4) − (2 × 2)
        = 4 − 4
        = 0

Comme det(A) = 0, la matrice n'est pas inversible.

==========================================================

""")
# Présente le critère de symétrie d'une matrice.
def verifier_symetrique_info()->None:
    print("""
==========================================================
           VÉRIFICATION D'UNE MATRICE SYMÉTRIQUE
==========================================================

Une matrice est dite symétrique si elle est égale à sa
transposée.

Condition :
• La matrice doit être carrée (même nombre de lignes
  et de colonnes).

Formule :

            A = Aᵀ

ou encore :

            aᵢⱼ = aⱼᵢ

Résultat :

• Si A = Aᵀ :
  → La matrice est symétrique.

• Si A ≠ Aᵀ :
  → La matrice n'est pas symétrique.
""")
# Affiche l'aide relative à l'addition de matrices.
def Addition_info()->None:
    print("""
==========================================================
                   INFORMATIONS SUR
              ADDITION DE DEUX MATRICES
==========================================================

L'addition de deux matrices est une opération qui consiste
à additionner les éléments situés à la même position dans
chaque matrice.

Pour que cette opération soit possible, les deux matrices
doivent avoir exactement les mêmes dimensions (même nombre
de lignes et même nombre de colonnes).

Le résultat est une nouvelle matrice dont chaque élément est
la somme des éléments correspondants des deux matrices.

Exemple :

A = ⎡1  2⎤      B = ⎡5  6⎤
    ⎣3  4⎦          ⎣7  8⎦

A + B = ⎡6   8⎤
        ⎣10 12⎦

Chaque élément est calculé comme suit :
1 + 5 = 6
2 + 6 = 8
3 + 7 = 10
4 + 8 = 12
==========================================================
""")
# Affiche l'aide relative à la soustraction de matrices.
def Soustraction_info()->None:
    print("""
==========================================================
             INFORMATIONS SUR LA SOUSTRACTION
                    DE DEUX MATRICES
==========================================================

La soustraction de deux matrices consiste à soustraire les
éléments correspondants de la deuxième matrice (B) de ceux
de la première matrice (A).

Condition :
• Les deux matrices doivent avoir le même nombre de lignes.
• Les deux matrices doivent avoir le même nombre de colonnes.

Formule :

            C = A - B

Chaque élément de la matrice résultat est calculé ainsi :

            C[i][j] = A[i][j] - B[i][j]

Exemple :

A = ⎡8  6⎤      B = ⎡3  2⎤
    ⎣5  4⎦          ⎣1  4⎦

A - B = ⎡8-3  6-2⎤ = ⎡5  4⎤
        ⎣5-1  4-4⎦   ⎣4  0⎦

Le résultat est une nouvelle matrice ayant les mêmes
dimensions que les deux matrices d'origine.

==========================================================
""")
# Affiche l'aide relative au produit de matrices.
def Multiplication_info()->None:
    print("""
==========================================================
          INFORMATIONS SUR LA MULTIPLICATION
                  DE DEUX MATRICES
==========================================================

La multiplication de deux matrices consiste à combiner les
lignes de la première matrice (A) avec les colonnes de la
deuxième matrice (B).

Condition :
• Le nombre de colonnes de la matrice A doit être égal
  au nombre de lignes de la matrice B.

Si A est de dimension (m × n), alors B doit être de
dimension (n × p).

Le résultat sera une matrice de dimension (m × p).

Formule :

            C = A × B

Chaque élément de la matrice résultat est obtenu en faisant
la somme des produits des éléments correspondants d'une
ligne de A et d'une colonne de B.

            C[i][j] = Σ (A[i][k] × B[k][j])

Exemple :

A = ⎡1  2⎤      B = ⎡5  6⎤
    ⎣3  4⎦          ⎣7  8⎦

Calcul :

C[1][1] = 1×5 + 2×7 = 19
C[1][2] = 1×6 + 2×8 = 22
C[2][1] = 3×5 + 4×7 = 43
C[2][2] = 3×6 + 4×8 = 50

Résultat :

A × B = ⎡19  22⎤
        ⎣43  50⎦

==========================================================
""")
def detKA ()->None:
    print("┌──────────────────────────────────────────────┐")
    print("│             Opérations effectuées            │")
    print("├──────────────────────────────────────────────┤")
    print("│               det(kA) = kⁿ det(A)            │")
    print("└──────────────────────────────────────────────┘")
    print()
# Affiche la formule utilisée pour calculer l'inverse d'une matrice.
def formul_inverse()->None:
    print("┌──────────────────────────────────────────────┐")
    print("│      FORMULE DE L'INVERSE D'UNE MATRICE      │")
    print("├──────────────────────────────────────────────┤")
    print("│        A⁻¹ = (1/det(A)) × com(A)ᵀ            │")
    print("└──────────────────────────────────────────────┘")
    print()
# Affiche l'aide détaillée relative à l'inverse d'une matrice.
def invers_info():
    print("""
==========================================================
                    INFORMATIONS SUR
                L'INVERSE D'UNE MATRICE
==========================================================

Définition :

L'inverse d'une matrice A est une matrice A⁻¹ telle que :

        A × A⁻¹ = A⁻¹ × A = I

où I est la matrice identité.

Conditions d'existence :

• La matrice doit être carrée.
• Son déterminant doit être non nul :
      det(A) ≠ 0

Formule :

        A⁻¹ = (1 / det(A)) × com(A)ᵀ

où :

• det(A)   : déterminant de la matrice A.
• com(A)   : comatrice (matrice des cofacteurs).
• com(A)ᵀ  : transposée de la comatrice (matrice adjointe).

Étapes de calcul :

1. Calculer le déterminant de A.
2. Vérifier que det(A) ≠ 0.
3. Calculer la comatrice.
4. Transposer la comatrice.
5. Multiplier chaque élément par 1 / det(A).

Remarque :

Si det(A) = 0, la matrice est dite singulière
et elle n'admet pas d'inverse.
==========================================================
""")
def rang_info():
    print("""
==========================================================
                INFORMATIONS SUR LE RANG
==========================================================

Le rang d'une matrice est le nombre maximal de lignes
(ou de colonnes) linéairement indépendantes.

En pratique, le rang est obtenu en réduisant la matrice
par la méthode de Gauss, puis en comptant le nombre de
lignes non nulles.

Conditions :

• La matrice doit être valide.
• Le rang est défini pour toute matrice carrée ou
  rectangulaire.
• Aucune condition d'inversibilité n'est requise.

Méthode de calcul :

1. Réduire la matrice par la méthode de Gauss.
2. Compter le nombre de lignes non nulles.
3. Ce nombre est le rang de la matrice.

Propriétés :

• 0 ≤ rg(A) ≤ min(n, m)

  où n est le nombre de lignes et m le nombre de
  colonnes.

• Si A est une matrice carrée d'ordre n :

      det(A) ≠ 0  ⇒  rg(A) = n

• Une matrice nulle possède un rang égal à 0.

• rg(A) = rg(Aᵀ)

• Le rang est égal au nombre de pivots de la matrice
  réduite.

Exemple 1 :

      ⎡1  2⎤
A =   ⎣2  4⎦

Après réduction :

      ⎡1  2⎤
      ⎣0  0⎦

Il reste une seule ligne non nulle.

rg(A) = 1

Exemple 2 :

      ⎡1  2⎤
A =   ⎣3  4⎦

Après réduction :

      ⎡1  2⎤
      ⎣0 -2⎦

Les deux lignes sont non nulles.

rg(A) = 2

==========================================================
""")
# Affiche l'aide relative à la multiplication par un scalaire.
def Multiplication_par_scalaire_info()->None:
    print("""
==========================================================
      INFORMATIONS SUR LA MULTIPLICATION
          D'UNE MATRICE PAR UN SCALAIRE
==========================================================

La multiplication d'une matrice par un scalaire consiste à
multiplier chacun de ses éléments par un même nombre réel
ou entier appelé scalaire.

Condition :
• La matrice peut être de n'importe quelle dimension.
• Le scalaire est un nombre (entier ou réel).

Formule :

            B = k × A

où :
• A est la matrice initiale.
• k est le scalaire.
• B est la matrice résultat.

Chaque élément est calculé ainsi :

            B[i][j] = k × A[i][j]

Exemple :

k = 3

A = ⎡1  2⎤
    ⎣3  4⎦

Calcul :

3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
3 × 4 = 12

Résultat :

3 × A = ⎡3   6 ⎤
        ⎣9  12⎦

La matrice résultat possède les mêmes dimensions que la
matrice initiale.

==========================================================
""")
# Affiche l'aide relative à la transposition d'une matrice.
def Transpose_info()->None:
    print("""
==========================================================
             INFORMATIONS SUR LA TRANSPOSÉE
                    D'UNE MATRICE
==========================================================

La transposée d'une matrice consiste à échanger ses lignes
et ses colonnes.

Autrement dit, l'élément situé à la ligne i et à la colonne
j devient l'élément situé à la ligne j et à la colonne i.

Formule :

            B = Aᵀ

Chaque élément est calculé ainsi :

            B[i][j] = A[j][i]

Si la matrice A est de dimension (m × n), alors sa
transposée Aᵀ sera de dimension (n × m).

Exemple :

A = ⎡1  2  3⎤
    ⎣4  5  6⎦

Après la transposition :

Aᵀ = ⎡1  4⎤
     ⎢2  5⎥
     ⎣3  6⎦

La transposition ne modifie pas les valeurs de la matrice,
elle change uniquement leur position.

==========================================================
""")
# Affiche l'aide relative à la puissance d'une matrice.
def puissance_info()->None:
    print("""
==========================================================
          INFORMATIONS SUR LA PUISSANCE
                 D'UNE MATRICE
==========================================================

La puissance d'une matrice consiste à multiplier une
matrice carrée par elle-même un certain nombre de fois.

Condition :
• La matrice doit être carrée (même nombre de lignes et
  de colonnes).
• L'exposant doit être un entier supérieur ou égal à 0.

Formule :

            B = Aⁿ

où :
• A est la matrice.
• n est l'exposant.

Exemples :

A¹ = A

A² = A × A

A³ = A × A × A

Cas particulier :

A⁰ = I

où I est la matrice identité de même dimension que A.

Exemple :

A = ⎡1  2⎤
    ⎣3  4⎦

A² = A × A

    = ⎡1  2⎤ × ⎡1  2⎤
      ⎣3  4⎦   ⎣3  4⎦

    = ⎡7   10⎤
      ⎣15  22⎦

Plus l'exposant est élevé, plus la matrice est multipliée
par elle-même.

==========================================================
""")
# Affiche l'aide relative à la réduction de Gauss.
def Reduction_Gauss_info():
    print("""
==========================================================
          INFORMATIONS SUR LA RÉDUCTION DE GAUSS
==========================================================

La réduction de Gauss est une méthode permettant de
transformer une matrice en une forme plus simple à l'aide
d'opérations élémentaires sur les lignes.

Cette méthode est utilisée pour :
• Résoudre un système d'équations linéaires.
• Déterminer le rang d'une matrice.
• Calculer l'inverse d'une matrice.
• Simplifier une matrice.

Opérations autorisées :

1. Échanger deux lignes.
2. Multiplier une ligne par un scalaire non nul.
3. Ajouter à une ligne un multiple d'une autre ligne.

Objectif :

Obtenir une matrice sous forme échelonnée, c'est-à-dire une
matrice où les pivots sont disposés en escalier et où les
éléments situés sous chaque pivot sont nuls.

Exemple :

Matrice initiale :

⎡1  2  1⎤
⎢2  4  3⎥
⎣3  6  5⎦

Après réduction de Gauss :

⎡1  2  1⎤
⎢0  0  1⎥
⎣0  0  0⎦

Une fois la réduction terminée, il devient plus facile
d'analyser la matrice ou de résoudre le système associé.

==========================================================
""")
# Affiche l'aide relative à la trace d'une matrice.
def diagonale_info()-> None:
    print("""
==========================================================
           INFORMATIONS SUR LA MATRICE DIAGONALE
==========================================================

Une matrice diagonale est une matrice carrée dont tous les
éléments en dehors de la diagonale principale sont nuls.

Condition :
• La matrice doit être carrée.
• Pour tout i ≠ j : aᵢⱼ = 0.

Forme générale :

        ⎡ d₁   0   0   ⋯   0 ⎤
        ⎢  0  d₂   0   ⋯   0 ⎥
    A = ⎢  0   0  d₃   ⋯   0 ⎥
        ⎢  ⋮   ⋮   ⋮   ⋱   ⋮ ⎥
        ⎣  0   0   0   ⋯  dₙ ⎦

Exemple :

        ⎡ 5   0   0 ⎤
        ⎢ 0  -2   0 ⎥
        ⎣ 0   0   7 ⎦

Propriétés :
• Une matrice diagonale est toujours symétrique.
• Sa transposée est égale à elle-même.
• Son déterminant est le produit des éléments de la
  diagonale principale.
• Elle est inversible si tous les éléments de la diagonale
  sont non nuls.
• Sa trace est la somme des éléments de la diagonale
  principale.
==========================================================

""")
def Trace_info():
    print("""
==========================================================
             INFORMATIONS SUR LA TRACE
                    D'UNE MATRICE
==========================================================

La trace d'une matrice est la somme des éléments situés sur
sa diagonale principale.

Condition :
• La matrice doit être carrée (même nombre de lignes et de
  colonnes).

Formule :

            tr(A) = a₁₁ + a₂₂ + ... + aₙₙ

où aᵢᵢ représente les éléments de la diagonale principale.

Exemple :

A = ⎡1  2  3⎤
    ⎢4  5  6⎥
    ⎣7  8  9⎦

Diagonale principale :

1, 5, 9

Calcul :

tr(A) = 1 + 5 + 9 = 15

La trace est un nombre réel ou entier, et non une matrice.

==========================================================
""")
# Affiche l'aide relative au calcul du déterminant.
def determinant_info():
    print("""
==========================================================
          INFORMATIONS SUR LE DÉTERMINANT
==========================================================

Le déterminant est un nombre associé à une matrice carrée.
Il permet notamment de savoir si une matrice est inversible,
de résoudre certains systèmes linéaires et de simplifier
plusieurs calculs grâce à ses propriétés.

Condition :
• La matrice doit être carrée (même nombre de lignes et de
  colonnes).

----------------------------------------------------------
1. Déterminant d'une matrice
----------------------------------------------------------

Noté :

        det(A)

Exemple (2 × 2) :

      ⎡a  b⎤
A =   ⎣c  d⎦

det(A) = ad − bc

----------------------------------------------------------
2. Déterminant de la transposée
----------------------------------------------------------

        det(Aᵀ) = det(A)

La transposition d'une matrice ne modifie pas son
déterminant.

----------------------------------------------------------
3. Déterminant d'un produit
----------------------------------------------------------

        det(AB) = det(A) × det(B)

Les deux matrices doivent être carrées et de même ordre.

----------------------------------------------------------
4. Déterminant d'une matrice multipliée
   par un scalaire
----------------------------------------------------------

        det(kA) = kⁿ × det(A)

où :
• k est un scalaire.
• n est l'ordre de la matrice.

----------------------------------------------------------
5. Déterminant de l'inverse
----------------------------------------------------------

        det(A⁻¹) = 1 / det(A)

Condition :
• A doit être inversible.
• det(A) ≠ 0.

----------------------------------------------------------
6. Déterminant de la matrice identité
----------------------------------------------------------

        det(Iₙ) = 1

où Iₙ désigne la matrice identité d'ordre n.

----------------------------------------------------------
Autres propriétés importantes
----------------------------------------------------------

• Si det(A) ≠ 0, alors A est inversible.
• Si det(A) = 0, alors A est singulière
  (non inversible).
• Échanger deux lignes change le signe du déterminant.
• Multiplier une ligne par k multiplie le déterminant
  par k.
• Si une ligne ou une colonne est nulle,
  alors det(A) = 0.
• Si deux lignes ou deux colonnes sont identiques,
  alors det(A) = 0.
• Le déterminant d'une matrice triangulaire est le
  produit des éléments de sa diagonale principale.

----------------------------------------------------------
Exemple
----------------------------------------------------------

      ⎡1  2⎤
A =   ⎣3  4⎦

det(A) = (1 × 4) − (2 × 3)
        = 4 − 6
        = −2

==========================================================
""")