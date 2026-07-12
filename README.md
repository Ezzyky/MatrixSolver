<div align="center">
  <img src="icon.ico" alt="Matrice icon" width="160" height="160" />

  # MatrixSolver

  An interactive Python command-line application for linear algebra — build matrices and apply a wide range of operations through a clean, menu-driven interface.

  ![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
  ![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)
  ![No dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)
  ![CLI](https://img.shields.io/badge/interface-CLI-informational)
  ![Status](https://img.shields.io/badge/status-in%20development-orange)
  ![License](https://img.shields.io/badge/license-MIT-green)
</div>

---

## About

**MatrixSolver** is an interactive CLI application for linear algebra. Build a matrix and apply operations to it — addition, multiplication, Gaussian elimination, determinants, and more — through a text menu, with every step (pivots, row operations, cofactors) printed along the way so you can follow the calculation, not just get the result.

It supports matrices with integer and real (float) coefficients, keeps a session history of every operation performed, and can export any result to a dated `.txt` report. It's available both as a Python script and as a standalone executable for Windows and Linux.

## Features

### 🔢 Matrix operations
- Addition and subtraction
- Multiplication (matrix × matrix, matrix × scalar)
- Transpose (Aᵀ)
- Matrix power (Aⁿ)

### 🧮 Reduction & solving
- Gaussian elimination, with each row operation displayed step by step
- Rank computation
- *Coming soon:* Gauss-Jordan method, linear system solving

### 📊 Properties & analysis
- Determinant, including its properties: det(Aᵀ), det(AB), det(kA), det(A⁻¹)
- Invertibility check
- Symmetry check
- Diagonal matrix check
- Trace
- Inverse (via the cofactor/adjugate method)

### 🚧 Advanced linear algebra *(planned)*
- Eigenvalues & eigenvectors
- Kernel Ker(A) & Image Im(A)
- LU decomposition
- SVD

### 🛠️ Quality-of-life
- Step-by-step calculation breakdown for every operation (pivots, row swaps, cofactors, etc.)
- Built-in explanations for each operation, with definitions, formulas, and worked examples
- Session history of all operations performed
- Export any result to a dated, formatted `.txt` report
- Input validation with clear, French error messages for invalid dimensions or incompatible operations



