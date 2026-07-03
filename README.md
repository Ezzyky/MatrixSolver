<img src="matrix.ico" alt="Matrice icon" width="48" height="48" />

# Matrice

A simple Python command-line tool that performs **Gaussian elimination** on a user-provided matrix, reducing it step by step to row-echelon form.

## Features

- Interactive matrix input (choose the number of rows and columns, then enter each value)
- Displays the matrix before and after elimination
- Automatically swaps rows if the first pivot is zero
- Performs Gaussian elimination using integer-only arithmetic (cross-multiplication instead of division, so no fractions appear during the process)

## Requirements

- Python 3
- No external dependencies

## Usage

Run the program from the project directory:

```bash
python main.py
```

You'll be prompted to:

1. Enter the number of rows and columns of your matrix
2. Enter each value of the matrix, one by one
3. View the original matrix
4. View the matrix after Gaussian elimination

### Example

```
Nombre de lignes : 3
Nombre de colonnes : 3
...
```

## Project structure

```
matrice/
├── main.py         # Entry point: builds the matrix and runs elimination
├── functions.py    # Core functions: input, display, and elimination logic
└── README.md
```

## How it works

`functions.py` contains three main functions:

- **`prenant_matrice()`** — prompts the user for matrix dimensions and values, returns the matrix as a list of lists
- **`affichage(matrice)`** — prints the matrix row by row
- **`elimination_gauss(matrice, pivot)`** — eliminates the entries below a given pivot using the formula:

  ```
  row[j][i] = row[j][i] * pivot_value - row[pivot][i] * factor
  ```

  This keeps all values as integers throughout the process instead of introducing decimals/fractions.

`main.py` ties it together: it builds the matrix, swaps rows if needed to avoid a zero pivot in the first position, then applies `elimination_gauss` for each pivot column.

## Known limitations

- Zero-pivot handling only checks the very first pivot; a zero pivot appearing later in the process is not automatically fixed by a row swap
- Values can grow large for bigger matrices since no division/simplification step is applied
- The result is a scaled row-echelon form, not a fully reduced one

## License

No license specified yet.
