# Matrice â€” Ã‰limination de Gauss en Python

Un programme Python en ligne de commande pour effectuer la **rÃ©duction d'une matrice par la mÃ©thode d'Ã©limination de Gauss** (mÃ©thode du pivot).

---

## FonctionnalitÃ©s

- Saisie interactive d'une matrice de taille quelconque (n Ã— m)
- Affichage formatÃ© de la matrice Ã  chaque Ã©tape
- Permutation automatique des lignes si le premier pivot est nul
- Ã‰limination de Gauss Ã©tape par Ã©tape jusqu'Ã  la forme Ã©chelonnÃ©e

---

## Structure du projet

```
matrice/
â”œâ”€â”€ functions.py   # Fonctions utilitaires (saisie, affichage, Ã©limination)
â””â”€â”€ main.py        # Programme principal
```

---

## Utilisation

```bash
python main.py
```

Le programme vous demandera de saisir la taille de la matrice, puis ses coefficients un par un :

```
Saisissez la taille de la matrice:
Nombre de lignes : 3
Nombre de colonnes : 3
M[1][1] = 2
M[1][2] = 1
...
```

---

## Exemple

Pour la matrice :

```
2  1 -1
-3 -1  2
-2  1  2
```

Le programme applique l'Ã©limination de Gauss et affiche la matrice Ã  chaque Ã©tape jusqu'Ã  obtenir la forme Ã©chelonnÃ©e.

---

## Algorithme

L'Ã©limination utilise la formule suivante pour chaque ligne `j` sous le pivot `p` :

```
L_j â† L_j Ã— pivot - L_pivot Ã— a
```

oÃ¹ `a = M[j][pivot]`. Cette approche Ã©vite les divisions et conserve des valeurs entiÃ¨res tout au long du calcul.

---

## PrÃ©requis

- Python 3.x
- Aucune bibliothÃ¨que externe requise

---

## Auteur

**Ezzyky** â€” [github.com/Ezzyky](https://github.com/Ezzyky)
