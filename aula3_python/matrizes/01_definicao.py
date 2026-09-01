"""
1) Definicao de matriz: arranjo retangular de numeros dispostos em m linhas
e n colunas (ordem m x n).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import mostrar_matriz


def main(outdir="resultados"):
    print("=" * 60)
    print("1) DEFINICAO DE MATRIZ")
    print("=" * 60)
    print("Uma matriz A = [aij] de ordem m x n e uma tabela retangular com")
    print("m linhas e n colunas, onde aij e o elemento da linha i e coluna j.")
    print()

    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    m, n = A.shape

    print(f"A =\n{A}")
    print(f"Ordem de A: {m} x {n}")
    print(f"a12 (linha 1, coluna 2) = {A[0, 1]}")
    print(f"a23 (linha 2, coluna 3) = {A[1, 2]}")

    fig, ax = plt.subplots(figsize=(4, 3))
    mostrar_matriz(ax, A, f"Matriz A ({m}x{n})")
    plt.tight_layout()
    fig.savefig(f"{outdir}/01_definicao.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/01_definicao.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
