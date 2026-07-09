from time import strftime,localtime
from colorama import *
init(autoreset=True)
time=strftime("%d-%m-%Y", localtime())
def menu()->None:
    print(f"""
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
    {Fore.BLUE+"[23]. historique "}              {Fore.GREEN+"[24]. Infos"}             {Fore.RED+"[0]. Quitter"}
                                                                                           
""")

def home()->None:
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

        Veuillez d'abord saisir la matrice initiale, puis choisir l'opération
        souhaitée dans le menu suivant.
    
            ========================================================== 
                                  -> REMARQUE <-
           
        Ce programme accepte uniquement des matrices à coefficients entiers.
        Les nombres réels (float) ne sont pas pris en charge.
            ==========================================================

    """)
def infos()->None:
    print(f"""
        Nom            : Abdellah
        Nationalité    : Marocaine
        Statut         : Étudiant en informatique

        Description :
        Ce programme a été développé en Python dans le cadre d'un
        projet d'algèbre linéaire. Il permet d'effectuer plusieurs
        opérations sur les matrices et les systèmes linéaires.
        i start at     : Jun 24, 2026
        i end at       : _

        Contact :
        E-mail         : Abdellahezzyky@gmail.com
        GitHub         : https://github.com/EZZYKY
        linkedin       : www.linkedin.com/in/abdellah-ezzyky-92b09a326
        Version        : 1.0
        Langage        : Python
""")
def titre(txte:str)->None:
    print()
    print("="*60)
    print(txte.center(60))
    print("="*60)
    print("\n")

def sous_menu()->None:
    print(f"""
  ========================================================== 
[1]. Sauvegarder dans "{time}.txt"                                   
[2]. Historique                                   {Fore.RED+"[0]. Retour "}{Style.RESET_ALL}
[3]. Explications         """)

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
def Addition_info()->None:
    print("""
==========================================================
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
    
def formul_inverse()->None:
    print("┌──────────────────────────────────────────────┐")
    print("│      FORMULE DE L'INVERSE D'UNE MATRICE      │")
    print("├──────────────────────────────────────────────┤")
    print("│                                              │")
    print("│        A⁻¹ = (1/det(A)) × com(A)ᵀ            │")
    print("│                                              │")
    print("│  • det(A) ≠ 0                                │")
    print("│  • com(A) : matrice des cofacteurs           │")
    print("│  • com(A)ᵀ : matrice adjointe                │")
    print("│                                              │")
    print("└──────────────────────────────────────────────┘")
    print()
def invers_info():
    print("""
==========================================================
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
def determinant_info():
    print("""
==========================================================
          INFORMATIONS SUR LE DÉTERMINANT
==========================================================

Le déterminant est un nombre associé à une matrice carrée.
Il permet notamment de savoir si une matrice est inversible
et de résoudre certains systèmes linéaires.

Condition :
• La matrice doit être carrée (même nombre de lignes et de
  colonnes).

Formules :

Pour une matrice 2 × 2 :

      ⎡a  b⎤
A =   ⎣c  d⎦

det(A) = ad − bc

Pour une matrice 3 × 3 :

      ⎡a  b  c⎤
A =   ⎢d  e  f⎥
      ⎣g  h  i⎦

det(A) = aei + bfg + cdh − ceg − bdi − afh

Propriétés :

• Si det(A) ≠ 0, la matrice est inversible.
• Si det(A) = 0, la matrice est singulière
  (non inversible).
• Échanger deux lignes change le signe du déterminant.
• Si une ligne est nulle, alors det(A) = 0.
• det(Aᵀ) = det(A).

Exemple :

      ⎡1  2⎤
A =   ⎣3  4⎦

Calcul :

det(A) = (1 × 4) − (2 × 3)
        = 4 − 6
        = −2

Le déterminant est un nombre réel ou entier, et non une
matrice.

==========================================================
""")
