def menu()->None:
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
   [11]. Déterminant                                    [17]. Valeurs propres
   [12]. Inverse                                        [18]. Vecteurs propres
   [13]. Trace                                          [19]. Noyau Ker(A)
   [14]. Vérifier inversible                            [20]. Image Im(A)
   [15]. Vérifier symétrique                            [21]. Décomposition LU
   [16]. Vérifier diagonale                             [22]. SVD


[E] Outils
   [23]. Historique                  
   [24]. Infos                                   
   [0]. Quitter                                           
""")

def home()->None:
     print("""
           
            ___  ___     ___       _       ____        _                
            |  \/  | __ _| |_ _ __(_)_  __/ ___|  ___ | |_   _____ _ __ 
            | |\/| |/ _` | __| '__| \ \/ /\___ \ / _ \| \ \ / / _ \ '__|
            | |  | | (_| | |_| |  | |>  <  ___) | (_) | |\ V /  __/ |   
            |_|  |_|\__,_|\__|_|  |_/_/\_\|____/ \___/|_| \_/ \___|_|

            Ce programme permet d'effectuer plusieurs opérations sur
            les matrices et les systèmes linéaires.

            Veuillez d'abord saisir la matrice initiale, puis choisir
            l'opération souhaitée dans le menu suivant.
           
            ========================================================== 
           
                                  -> REMARQUE <-
            Ce programme accepte uniquement des matrices à coefficients
            entiers.
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
    print("="*60)
    print(txte.center(60))
    print("="*60)
    print("\n")

def sous_menu()->None:
    print("""
  ========================================================== 
[1]. Sauvegarder                                    [3]. Infos
[2]. Historique                                     [0]. Quitter""")

