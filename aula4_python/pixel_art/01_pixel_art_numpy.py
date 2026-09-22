"""
1) Pixel art 8x8 (cogumelo) construida do zero com matrizes NumPy (altura x largura x RGB).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main(outdir="resultados"):
    print("=" * 60)
    print("1) PIXEL ART 8x8 VIA MATRIZES NUMPY")
    print("=" * 60)

    indices = np.array([
        [0, 0, 4, 4, 4, 4, 0, 0],
        [0, 4, 1, 1, 1, 1, 4, 0],
        [4, 1, 1, 2, 2, 1, 1, 4],
        [4, 1, 2, 1, 1, 2, 1, 4],
        [4, 4, 4, 4, 4, 4, 4, 4],
        [0, 4, 3, 3, 3, 3, 4, 0],
        [0, 4, 3, 3, 3, 3, 4, 0],
        [0, 0, 4, 4, 4, 4, 0, 0],
    ])

    paleta = np.array([
        [1.00, 1.00, 1.00],
        [0.85, 0.10, 0.10],
        [1.00, 1.00, 1.00],
        [0.96, 0.87, 0.70],
        [0.00, 0.00, 0.00],
    ])

    imagem = paleta[indices]

    print(f"Dimensoes da matriz de indices: {indices.shape}")
    print(f"Dimensoes da imagem RGB: {imagem.shape}")
    print(f"Paleta de cores (0=fundo, 1=vermelho, 2=branco, 3=creme, 4=preto):\n{paleta}")

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(imagem, interpolation="nearest")
    ax.set_xticks(np.arange(-0.5, 8, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 8, 1), minor=True)
    ax.grid(which="minor", color="gray", linewidth=0.7)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Pixel Art 8x8 - Cogumelo")

    plt.tight_layout()
    fig.savefig(f"{outdir}/01_pixel_art_numpy.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/01_pixel_art_numpy.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
