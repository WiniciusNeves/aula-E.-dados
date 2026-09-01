"""
10) Determinante por cofatores (Teorema de Laplace), para uma matriz 4x4.
"""
import numpy as np


def menor_complementar(A, i, j):
    return np.delete(np.delete(A, i, axis=0), j, axis=1)


def determinante_cofatores(A):
    n = A.shape[0]
    if n == 1:
        return A[0, 0]
    if n == 2:
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]

    det = 0.0
    for j in range(n):
        cofator = ((-1) ** (0 + j)) * determinante_cofatores(menor_complementar(A, 0, j))
        det += A[0, j] * cofator
    return det


def main(outdir="resultados"):
    print("=" * 60)
    print("10) DETERMINANTE POR COFATORES (TEOREMA DE LAPLACE) - matriz 4x4")
    print("=" * 60)

    A = np.array([
        [1, 2, 3, 0],
        [0, 4, 5, 1],
        [1, 0, 6, 2],
        [2, 1, 0, 3],
    ], dtype=float)

    det_manual = determinante_cofatores(A)
    det_numpy = np.linalg.det(A)

    print(f"A =\n{A}")
    print(f"\nExpandindo pela primeira linha:")
    print(f"det(A) = a11.C11 + a12.C12 + a13.C13 + a14.C14")
    print(f"\ndet(A) calculado por cofatores (implementacao manual) = {det_manual:.4f}")
    print(f"det(A) calculado pelo numpy (conferencia)              = {det_numpy:.4f}")
    print(f"Resultados batem? {np.isclose(det_manual, det_numpy)}")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
