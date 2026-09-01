"""
8) Matriz inversa (dimensao maior que 3x3): A^-1 tal que A.A^-1 = A^-1.A = I.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import mostrar_matriz


def main(outdir="resultados"):
    print("=" * 60)
    print("8) MATRIZ INVERSA (4x4)")
    print("=" * 60)

    A = np.array([
        [4, 1, 2, 1],
        [1, 5, 1, 2],
        [2, 1, 6, 1],
        [1, 2, 1, 7],
    ], dtype=float)

    det = np.linalg.det(A)
    print(f"A =\n{A}")
    print(f"det(A) = {det:.4f}")

    A_inv = np.linalg.inv(A)
    print(f"\nA^-1 =\n{np.round(A_inv, 4)}")

    verificacao = A @ A_inv
    print(f"\nA . A^-1 (deve ser a identidade) =\n{np.round(verificacao, 4)}")
    print(f"E igual a identidade? {np.allclose(verificacao, np.eye(4))}")

    fig, axs = plt.subplots(1, 3, figsize=(13, 4))
    mostrar_matriz(axs[0], A, "A")
    mostrar_matriz(axs[1], A_inv, "A inversa")
    mostrar_matriz(axs[2], np.round(verificacao, 4), "A . A^-1 = I", destacar_diagonal=True)
    plt.tight_layout()
    fig.savefig(f"{outdir}/08_inversa.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/08_inversa.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
