"""
4) Cisalhamento (Shear): inclinar o espaco, como empurrar o topo de um
baralho de cartas.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import quadrado_unitario, aplicar_transformacao, plotar_antes_depois


def main(outdir="resultados"):
    print("=" * 60)
    print("4) CISALHAMENTO (SHEAR)")
    print("=" * 60)

    k = 0.75
    M_shear = np.array([[1, k], [0, 1]])

    print(f"Fator de cisalhamento k = {k}")
    print(f"Matriz de cisalhamento M =\n{M_shear}")

    antes = quadrado_unitario()
    depois = aplicar_transformacao(M_shear, antes)

    fig, ax = plt.subplots(figsize=(5, 5))
    plotar_antes_depois(ax, antes, depois, f"Cisalhamento horizontal com k = {k}")
    plt.tight_layout()
    fig.savefig(f"{outdir}/04_cisalhamento.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/04_cisalhamento.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
