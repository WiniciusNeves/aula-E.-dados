"""
8) Vetores linearmente independentes (LI) x linearmente dependentes (LD).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import vt


def classificar(v1, v2):
    matriz = np.array([v1, v2])
    det = np.linalg.det(matriz)
    rank = np.linalg.matrix_rank(matriz)
    dependentes = np.isclose(det, 0)
    return det, rank, dependentes


def main(outdir="resultados"):
    print("=" * 60)
    print("8) VETORES LINEARMENTE INDEPENDENTES (LI) x DEPENDENTES (LD)")
    print("=" * 60)
    print("Vetores sao LI quando a unica combinacao a.v1 + b.v2 = 0 e a=b=0.")
    print("Isso equivale a det([v1, v2]) != 0 (matriz de posto completo).")
    print()

    # Caso A: v2 e multiplo de v1 -> LD (colineares)
    v1_ld = np.array([2, 1])
    v2_ld = np.array([4, 2])

    # Caso B: vetores nao colineares -> LI
    v1_li = np.array([2, 1])
    v2_li = np.array([1, 3])

    det_ld, rank_ld, dep_ld = classificar(v1_ld, v2_ld)
    det_li, rank_li, dep_li = classificar(v1_li, v2_li)

    print("Caso A (colineares):")
    print(f"  v1 = {vt(v1_ld)}   v2 = {vt(v2_ld)}")
    print(f"  det = {det_ld:.4f}   posto(rank) = {rank_ld}   -> {'LD' if dep_ld else 'LI'}")
    print()
    print("Caso B (nao colineares):")
    print(f"  v1 = {vt(v1_li)}   v2 = {vt(v2_li)}")
    print(f"  det = {det_li:.4f}   posto(rank) = {rank_li}   -> {'LD' if dep_li else 'LI'}")

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    def desenhar(ax, v1, v2, titulo):
        ax.quiver(0, 0, v1[0], v1[1], angles="xy", scale_units="xy", scale=1, color="tab:blue", label="v1")
        ax.quiver(0, 0, v2[0], v2[1], angles="xy", scale_units="xy", scale=1, color="tab:orange", label="v2")
        limite = max(abs(v1).max(), abs(v2).max()) + 1
        ax.set_xlim(-1, limite)
        ax.set_ylim(-1, limite)
        ax.set_aspect("equal")
        ax.grid(True)
        ax.axhline(0, color="black", linewidth=0.5)
        ax.axvline(0, color="black", linewidth=0.5)
        ax.set_title(titulo)
        ax.legend()

    desenhar(axs[0], v1_ld, v2_ld, "LD: v2 = 2.v1 (colineares)")
    desenhar(axs[1], v1_li, v2_li, "LI: v1 e v2 nao colineares")

    plt.tight_layout()
    fig.savefig(f"{outdir}/08_dependencia_linear.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/08_dependencia_linear.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
