#  Matrice — Calcul Matriciel en Python

Un projet Python permettant de saisir, afficher et appliquer l'**élimination de Gauss** sur une matrice, avec permutation automatique des lignes pour garantir un pivot non nul.

---

##  Structure du projet

```
matrice/
├── functions.py   # Fonctions : saisie, affichage, élimination de Gauss
└── main.py        # Programme principal : exécution et affichage étape par étape
```

---

##  Fonctionnalités

- **Saisie interactive** — l'utilisateur entre la taille et les valeurs de la matrice
- **Affichage formaté** — affichage clair de la matrice après chaque opération
- **Permutation de lignes** — échange automatique si le premier pivot est nul
- **Élimination de Gauss** — triangularisation de la matrice (méthode du pivot)

---

##  Utilisation

### Prérequis

- Python 3.x

### Lancer le programme

```bash
python main.py
```

### Exemple d'exécution

```
Saisissez la taille de la matrice:
Nombre de lignes : 3
Nombre de colonnes : 3
M[1][1] = 0
M[1][2] = 2
M[1][3] = 1
...

L1 ↔ L2

2 1 0
0 2 1
0 0 3
```

---

##  Fonctions principales (`functions.py`)

| Fonction | Description |
|---|---|
| `prenant_matrice()` | Saisie interactive d'une matrice de taille n×m |
| `affichage(matrice)` | Affichage ligne par ligne de la matrice |
| `elimination_gauss(matrice, pivot)` | Applique un pas d'élimination de Gauss au pivot donné |

---

##  Concepts utilisés

- Listes 2D (matrices en Python)
- Algorithmique : méthode du pivot de Gauss
- Programmation modulaire (séparation fonctions / main)

---

##  Auteur

**Abdellah Ezzyky** — Étudiant en Informatique Appliquée, Faculté des Sciences d'El Jadida

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/abdellah-ezzyky-92b09a326)
[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/Ezzyky)
