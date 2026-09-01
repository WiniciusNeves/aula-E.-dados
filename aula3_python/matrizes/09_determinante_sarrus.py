"""
9) Determinante pela Regra de Sarrus.

OBS.: a Regra de Sarrus e um metodo mnemonico valido apenas para matrizes
3x3 (nao existe uma versao valida de Sarrus para ordem > 3). Por isso o
exemplo abaixo usa uma matriz 3x3; o calculo para matrizes maiores (4x4) e
feito por cofatores/Laplace no proximo script (10_determinante_cofatores.py).
"""
import numpy as np


def determinante_sarrus(A):
    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]
    return (a * e * i + b * f * g + c * d * h) - (c * e * g + a * f * h + b * d * i)


def main(outdir="resultados"):
    print("=" * 60)
    print("9) DETERMINANTE PELA REGRA DE SARRUS (3x3)")
    print("=" * 60)

    A = np.array([[1, 2, 3], [0, 4, 5], [1, 0, 6]])
    det_sarrus = determinante_sarrus(A)
    det_numpy = np.linalg.det(A)

    print(f"A =\n{A}")
    print(f"det(A) pela Regra de Sarrus = {det_sarrus}")
    print(f"det(A) pelo numpy (conferencia) = {det_numpy:.4f}")
    print(f"Resultados batem? {np.isclose(det_sarrus, det_numpy)}")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
