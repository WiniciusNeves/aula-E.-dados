"""
12) Matriz adjunta: adj(A) = (cof(A))^T. Vale A^-1 = adj(A) / det(A).
Exemplo com matriz 4x4.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import mostrar_matriz


def menor_complementar(A, i, j):
    return np.delete(np.delete(A, i, axis=0), j, axis=1)


def matriz_cofatores(A):
    n = A.shape[0]
    C = np.zeros_like(A)
    for i in range(n):
        for j in range(n):
            C[i, j] = ((-1) ** (i + j)) * np.linalg.det(menor_complementar(A, i, j))
    return C


def main(outdir="resultados"):
    print("=" * 60)
    print("12) MATRIZ ADJUNTA (4x4)")
    print("=" * 60)

    A = np.array([
        [4, 1, 2, 1],
        [1, 5, 1, 2],
        [2, 1, 6, 1],
        [1, 2, 1, 7],
    ], dtype=float)

    det = np.linalg.det(A)
    cof = matriz_cofatores(A)
    adj = cof.T
    A_inv_via_adj = adj / det
    A_inv_numpy = np.linalg.inv(A)

    print(f"A =\n{A}")
    print(f"det(A) = {det:.4f}")
    print(f"\nMatriz de cofatores cof(A) =\n{np.round(cof, 4)}")
    print(f"\nMatriz adjunta adj(A) = cof(A)^T =\n{np.round(adj, 4)}")
    print(f"\nA^-1 = adj(A)/det(A) =\n{np.round(A_inv_via_adj, 4)}")
    print(f"\nA^-1 pelo numpy (conferencia) =\n{np.round(A_inv_numpy, 4)}")
    print(f"Resultados batem? {np.allclose(A_inv_via_adj, A_inv_numpy)}")

    fig, axs = plt.subplots(1, 3, figsize=(13, 4))
    mostrar_matriz(axs[0], A, "A")
    mostrar_matriz(axs[1], np.round(adj, 2), "adj(A)")
    mostrar_matriz(axs[2], np.round(A_inv_via_adj, 3), "A^-1 = adj(A)/det(A)")
    plt.tight_layout()
    fig.savefig(f"{outdir}/12_adjunta.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/12_adjunta.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
