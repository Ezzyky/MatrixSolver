<div align="center">
  <img src="matrix.ico" alt="Matrice icon" width="160" height="160" />

  # MatrixSolver

  A Python command-line application for linear algebra — perform matrix operations, Gaussian elimination, and more through an interactive menu.

  ![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
  ![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)
  ![No dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)
  ![CLI](https://img.shields.io/badge/interface-CLI-informational)
  ![Status](https://img.shields.io/badge/status-in%20development-orange)
</div>

---

## Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Installation & Usage](#installation--usage)
- [Example](#example)
- [Project structure](#project-structure)
- [How it works](#how-it-works)
- [Roadmap](#roadmap)
- [Known limitations](#known-limitations)
- [License](#license)

## About

**Matrice** is an interactive CLI application that lets you build a matrix and apply a range of linear algebra operations to it through a text menu — addition, subtraction, multiplication, Gaussian elimination, and more. Only integer-coefficient matrices are supported. It's available both as a Python script and as a standalone Windows executable (`MatrixSolver.exe`).

## Features

### ✅ Implemented

**Matrix operations**
- Addition
- Subtraction
- Multiplication
- Scalar multiplication
- Transpose

**Reduction**
- Gaussian elimination (row-echelon form), with row-swap handling for zero pivots and a step-by-step printout of every row operation performed (e.g. `L2 ← 2L2 - 3L1`)

**Analysis**
- Trace

**Tools**
- Operation history tracking (session-based)
- App info / author details screen

### 🚧 Planned (present in the menu, not yet implemented)

- Gauss-Jordan method
- Linear system solving
- Rank
- Determinant
- Inverse
- Invertibility / symmetry / diagonality checks
- Eigenvalues & eigenvectors
- Kernel (Ker) and Image (Im)
- LU decomposition
- SVD
- Save/export results (submenu option is present but currently a no-op)

## Requirements

- Python 3 (only needed if running from source)
- No external dependencies — standard library only
- `os.system("cls")` is used for screen clearing in the main loop, so the Python version currently targets **Windows**

## Installation & Usage

### Option 1 — Run the standalone executable (Windows)

Download `MatrixSolver.exe` and run it directly — no Python installation required.

### Option 2 — Run from source

```bash
python main.py
```

Once running:

1. Enter the matrix you want to work with (dimensions, then each value)
2. Choose an operation from the menu
3. Provide any additional input the operation needs (e.g. a second matrix, a scalar)
4. View the result, then choose to save, view history, see app info, or quit from the sub-menu

## Example

```
Saisissez la taille de la matrice A:
Nombre de lignes : 3
Nombre de colonnes : 3
M[1][1] = 2
M[1][2] = 1
M[1][3] = -1
M[2][1] = -3
M[2][2] = -1
M[2][3] = 2
M[3][1] = -2
M[3][2] = 1
M[3][3] = 2

Matrice initiale :

⎡ 2 1 -1 ⎤
⎢ -3 -1 2 ⎥
⎣ -2 1 2 ⎦

_________Opérations effectuées sur les lignes :_________

L2 ← 2L2 + 3L1
L3 ← 2L3 + 2L1

--> Resulta finale:

⎡ 2 1 -1 ⎤
⎢ 0 1 1 ⎥
⎣ 0 0 10 ⎦
```

## Project structure

```
matrice/
├── main.py           # Entry point: menu loop, dispatches to each operation
├── matrice_io.py      # Matrix input, pretty-printed display, row swapping
├── gauss.py           # Gaussian elimination logic + printed row operations
├── operations.py      # Addition, subtraction, multiplication, scalar mult., transpose
├── analyse.py         # Matrix analysis functions (trace, and future ones)
├── menu_txtes.py      # All menu/text screens (home, menu, sub-menu, info, titles)
├── utils.py           # Helpers: clear screen, history, quit, sub-menu routing
├── MatrixSolver.exe   # Standalone compiled version (Windows)
├── matrix.ico         # App icon
└── README.md
```

## How it works

- **`matrice_io.py`** handles building a matrix from user input (`prenant_matrice`, wrapped by `demander_matrice` which retries on invalid input via a custom `MatrixSizeError`), and displaying it with bracket-style formatting (`affichage`).
- **`operations.py`** implements the basic matrix arithmetic (`addition`, `souetraction`, `multiplication`, `multiplication_scalaire`, `Transpose`), each printing the term-by-term calculation as it goes.
- **`gauss.py`** implements `elimination_gauss(matrice, pivot)`, which eliminates entries below a pivot using integer-only cross-multiplication (`row_j*pivot_value - row_pivot*factor`) instead of division, and prints each row operation in `L_j ← ...` notation.
- **`analyse.py`** holds matrix property functions — currently just `trace`, with room to grow into determinant, rank, etc.
- **`menu_txtes.py`** centralizes all the text screens (welcome screen, main menu, sub-menu, info screen, section titles).
- **`utils.py`** provides shared helpers: clearing the screen cross-platform, printing the operation history, handling the sub-menu's routing (`options`), and exiting the app.
- **`main.py`** ties everything together in a `while True` loop: it shows the menu, reads the chosen option, asks for the matrix (and any extra input the operation needs), runs the operation, displays the result, and then hands off to a sub-menu (save / history / info / quit) before looping back.

## Known limitations

- Several menu items are listed but not yet functional (see [Roadmap](#roadmap)) — selecting them either does nothing meaningful or falls through to the "pas de option!" message.
- The main loop uses `os.system("cls")` directly (Windows-only); only `clear_avec_msg` in `utils.py` checks the OS and supports `clear` on Linux/macOS.
- `multiplication_scalaire` accepts a `float` scalar even though the app is documented as integer-only, so results can contain decimals.
- If a matrix column has no nonzero entry at or below the pivot (a singular/rank-deficient matrix), Gaussian elimination has no fallback and may leave that pivot as zero without a clear message.
- The "Sauvegarder" (save) option in the sub-menu is present but currently does nothing (`pass`).
- Operation history is kept only for the current session (not persisted to a file).


## License

No license specified yet.
