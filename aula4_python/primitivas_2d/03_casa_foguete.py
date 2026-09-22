"""
3) Composicao de uma casa combinando poligonos, retangulos e circulos.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle


def main(outdir="resultados"):
    print("=" * 60)
    print("3) COMPOSICAO: CASA")
    print("=" * 60)

    fig, ax = plt.subplots(figsize=(6, 6))

    corpo = Rectangle((-1.5, 0), width=3.0, height=2.0, color="wheat", zorder=1)
    telhado = Polygon([(-1.8, 2.0), (1.8, 2.0), (0, 3.2)], closed=True, color="firebrick", zorder=1)
    porta = Rectangle((-0.35, 0), width=0.7, height=1.2, color="saddlebrown", zorder=2)
    mac_porta = Circle((-0.08, 0.6), radius=0.04, color="gold", zorder=3)
    janela = Rectangle((0.6, 1.1), width=0.6, height=0.6, color="skyblue", zorder=2)
    chamine = Rectangle((0.9, 2.0), width=0.35, height=1.4, color="dimgray", zorder=1)

    for patch in [corpo, telhado, porta, mac_porta, janela, chamine]:
        ax.add_patch(patch)

    print("Corpo: retangulo (-1.5, 0) 3.0x2.0")
    print("Telhado: poligono [(-1.8,2.0),(1.8,2.0),(0,3.2)]")
    print("Porta: retangulo com mac (circulo)")
    print("Janela: retangulo; Chamine: retangulo")

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(0, 4)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_title("Composicao 2D: Casa")

    plt.tight_layout()
    fig.savefig(f"{outdir}/03_casa_foguete.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/03_casa_foguete.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
