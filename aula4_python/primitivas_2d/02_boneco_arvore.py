"""
2) Composicao de um boneco e de uma arvore combinando circulos e retangulos.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def desenhar_boneco(ax):
    cabeca = Circle((0, 3.3), radius=0.5, color="peachpuff", zorder=3)
    tronco = Rectangle((-0.35, 1.6), width=0.7, height=1.6, color="royalblue", zorder=2)
    braco_esquerdo = Rectangle((-0.85, 2.3), width=0.5, height=0.25, color="peachpuff", zorder=2)
    braco_direito = Rectangle((0.35, 2.3), width=0.5, height=0.25, color="peachpuff", zorder=2)
    perna_esquerda = Rectangle((-0.32, 0.4), width=0.28, height=1.2, color="dimgray", zorder=2)
    perna_direita = Rectangle((0.04, 0.4), width=0.28, height=1.2, color="dimgray", zorder=2)

    for patch in [cabeca, tronco, braco_esquerdo, braco_direito, perna_esquerda, perna_direita]:
        ax.add_patch(patch)

    ax.set_xlim(-2, 2)
    ax.set_ylim(0, 4)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_title("Boneco")


def desenhar_arvore(ax):
    tronco = Rectangle((-0.25, 0), width=0.5, height=1.4, color="saddlebrown", zorder=2)
    copa_baixa = Circle((0, 2.0), radius=1.0, color="forestgreen", zorder=2)
    copa_alta = Circle((0, 2.8), radius=0.75, color="mediumseagreen", zorder=3)

    for patch in [tronco, copa_baixa, copa_alta]:
        ax.add_patch(patch)

    ax.set_xlim(-2, 2)
    ax.set_ylim(0, 4)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_title("Arvore")


def main(outdir="resultados"):
    print("=" * 60)
    print("2) COMPOSICAO: BONECO E ARVORE")
    print("=" * 60)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    desenhar_boneco(ax1)
    desenhar_arvore(ax2)

    print("Boneco: circulo (cabeca), retangulos (tronco, bracos, pernas)")
    print("Arvore: retangulo (tronco), circulos (copa em duas camadas)")

    plt.tight_layout()
    fig.savefig(f"{outdir}/02_boneco_arvore.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/02_boneco_arvore.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
