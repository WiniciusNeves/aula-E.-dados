"""
1) Rasterizacao de retas com o algoritmo de Bresenham (aritmetica de inteiros).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import bresenham


def main(outdir="resultados"):
    print("=" * 60)
    print("1) ALGORITMO DE BRESENHAM")
    print("=" * 60)

    altura, largura = 40, 60
    grid = np.zeros((altura, largura))

    segmentos = [
        ((2, 2), (57, 37)),
        ((5, 35), (50, 3)),
        ((2, 20), (57, 20)),
        ((30, 2), (30, 37)),
    ]

    for i, (p0, p1) in enumerate(segmentos, start=1):
        pontos = bresenham(p0[0], p0[1], p1[0], p1[1])
        print(f"Segmento {i}: {p0} -> {p1}  ({len(pontos)} pixels)")
        for (x, y) in pontos:
            grid[y, x] = i

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(grid, origin="lower", cmap="viridis", interpolation="nearest")
    ax.set_title("Retas rasterizadas com o algoritmo de Bresenham")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    plt.tight_layout()
    fig.savefig(f"{outdir}/01_linha_bresenham.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/01_linha_bresenham.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
