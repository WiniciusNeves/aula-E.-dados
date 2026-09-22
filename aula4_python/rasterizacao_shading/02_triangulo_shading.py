"""
2) Rasterizacao de triangulo preenchido (bounding box + coordenadas baricentricas)
   comparando Flat Shading e Gouraud Shading.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import rasterizar_triangulo


def main(outdir="resultados"):
    print("=" * 60)
    print("2) RASTERIZACAO DE TRIANGULO E SHADING")
    print("=" * 60)

    altura, largura = 60, 80
    v0, v1, v2 = (10, 50), (70, 50), (40, 8)

    cor_flat = np.array([0.85, 0.15, 0.15])
    imagem_flat = rasterizar_triangulo(v0, v1, v2, altura, largura, cores=[cor_flat, cor_flat, cor_flat])

    cores_vertices = [np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 0.0, 1.0])]
    imagem_gouraud = rasterizar_triangulo(v0, v1, v2, altura, largura, cores=cores_vertices)

    print(f"Vertices do triangulo: v0={v0}, v1={v1}, v2={v2}")
    print(f"Cor uniforme (Flat Shading): {cor_flat}")
    print(f"Cores dos vertices (Gouraud Shading): {cores_vertices}")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.5))
    ax1.imshow(imagem_flat, origin="lower")
    ax1.set_title("Flat Shading")
    ax2.imshow(imagem_gouraud, origin="lower")
    ax2.set_title("Gouraud Shading")

    plt.tight_layout()
    fig.savefig(f"{outdir}/02_triangulo_shading.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/02_triangulo_shading.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
