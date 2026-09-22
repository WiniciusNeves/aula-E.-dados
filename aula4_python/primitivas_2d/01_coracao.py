"""
1) Composicao de um coracao a partir de duas elipses rotacionadas e um poligono triangular.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon


def main(outdir="resultados"):
    print("=" * 60)
    print("1) COMPOSICAO: CORACAO")
    print("=" * 60)

    fig, ax = plt.subplots(figsize=(6, 6))

    lobo_esquerdo = Ellipse((-0.5, 0.55), width=1.1, height=1.4, angle=-45, color="crimson")
    lobo_direito = Ellipse((0.5, 0.55), width=1.1, height=1.4, angle=45, color="crimson")
    ponta = Polygon([(-1.05, 0.45), (1.05, 0.45), (0, -1.3)], closed=True, color="crimson")

    ax.add_patch(lobo_esquerdo)
    ax.add_patch(lobo_direito)
    ax.add_patch(ponta)

    print("Elipse esquerda: centro=(-0.5, 0.55), largura=1.1, altura=1.4, angulo=-45")
    print("Elipse direita:  centro=(0.5, 0.55), largura=1.1, altura=1.4, angulo=45")
    print("Poligono (ponta): vertices=[(-1.05, 0.45), (1.05, 0.45), (0, -1.3)]")

    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_title("Composicao 2D: Coracao")

    plt.tight_layout()
    fig.savefig(f"{outdir}/01_coracao.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/01_coracao.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
