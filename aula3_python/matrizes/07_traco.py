"""
7) Traco de uma matriz: soma dos elementos da diagonal principal.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import mostrar_matriz


def main(outdir="resultados"):
    print("=" * 60)
    print("7) TRACO DA MATRIZ")
    print("=" * 60)

    A = np.array([[4, 1, 2], [3, 5, 6], [7, 8, 9]])
    traco = np.trace(A)

    print(f"A =\n{A}")
    print(f"Diagonal principal: {np.diagonal(A).tolist()}")
    print(f"tr(A) = {' + '.join(map(str, np.diagonal(A)))} = {traco}")

    fig, ax = plt.subplots(figsize=(4, 4))
    mostrar_matriz(ax, A, f"A  (tr(A) = {traco})", destacar_diagonal=True)
    plt.tight_layout()
    fig.savefig(f"{outdir}/07_traco.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/07_traco.png (diagonal destacada em negrito)")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
