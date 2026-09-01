"""
5) Reflexao: espelhar o espaco em relacao a um eixo.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import quadrado_unitario, aplicar_transformacao, plotar_antes_depois


def main(outdir="resultados"):
    print("=" * 60)
    print("5) REFLEXAO")
    print("=" * 60)

    M_eixo_x = np.array([[1, 0], [0, -1]])   # reflete em torno do eixo x
    M_eixo_y = np.array([[-1, 0], [0, 1]])   # reflete em torno do eixo y
    M_origem = np.array([[-1, 0], [0, -1]])  # reflete em torno da origem

    print(f"Reflexao em torno do eixo x: M =\n{M_eixo_x}")
    print(f"Reflexao em torno do eixo y: M =\n{M_eixo_y}")
    print(f"Reflexao em torno da origem: M =\n{M_origem}")

    antes = quadrado_unitario()

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    plotar_antes_depois(axs[0], antes, aplicar_transformacao(M_eixo_x, antes), "Reflexao em torno do eixo x")
    plotar_antes_depois(axs[1], antes, aplicar_transformacao(M_eixo_y, antes), "Reflexao em torno do eixo y")
    plotar_antes_depois(axs[2], antes, aplicar_transformacao(M_origem, antes), "Reflexao em torno da origem")
    for ax in axs:
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)

    plt.tight_layout()
    fig.savefig(f"{outdir}/05_reflexao.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/05_reflexao.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
