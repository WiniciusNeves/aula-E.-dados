"""
1) Definicao de transformacao linear.

T: U -> V e uma transformacao linear se, para todo u, v em U e todo escalar
alpha, valem:
  T(u + v) = T(u) + T(v)      (aditividade)
  T(alpha.u) = alpha.T(u)     (homogeneidade)

Toda transformacao linear entre espacos de dimensao finita pode ser
representada por uma matriz A, de modo que T(x) = A.x.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import quadrado_unitario, aplicar_transformacao, plotar_antes_depois


def vt(v):
    return tuple(np.round(np.asarray(v, dtype=float), 4).tolist())



def main(outdir="resultados"):
    print("=" * 60)
    print("1) DEFINICAO DE TRANSFORMACAO LINEAR")
    print("=" * 60)
    print("T(x) = A.x, onde A e a matriz que representa a transformacao.")
    print()

    A = np.array([[2, 0], [0, 1]])  # exemplo simples: escala em x
    x = np.array([3, 2])
    Tx = A @ x

    print(f"Matriz A =\n{A}")
    print(f"x = {vt(x)}")
    print(f"T(x) = A.x = {vt(Tx)}")

    antes = quadrado_unitario()
    depois = aplicar_transformacao(A, antes)

    fig, ax = plt.subplots(figsize=(5, 5))
    plotar_antes_depois(ax, antes, depois, "T(x) = A.x  aplicada a um quadrado unitario")
    plt.tight_layout()
    fig.savefig(f"{outdir}/01_definicao.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/01_definicao.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
