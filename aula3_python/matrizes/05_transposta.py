"""
5) Matriz transposta: A^T e obtida transformando as linhas de A em colunas.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import mostrar_matriz


def main(outdir="resultados"):
    print("=" * 60)
    print("5) MATRIZ TRANSPOSTA")
    print("=" * 60)

    A = np.array([[2, 3], [1, 4], [5, 6]])
    At = A.T

    print(f"A ({A.shape[0]}x{A.shape[1]}) =\n{A}")
    print(f"\nA^T ({At.shape[0]}x{At.shape[1]}) =\n{At}")

    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
    mostrar_matriz(axs[0], A, "A")
    mostrar_matriz(axs[1], At, "A transposta (A^T)")
    plt.tight_layout()
    fig.savefig(f"{outdir}/05_transposta.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/05_transposta.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
