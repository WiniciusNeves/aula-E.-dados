"""
2) Modelagem 3D de um cubo e aplicacao de uma transformacao linear (rotacao + translacao)
   nos vertices via multiplicacao de matrizes, comparando antes e depois.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from _util import cubo_vertices, ARESTAS_CUBO, matriz_transformacao_3d, aplicar_transformacao_3d, plotar_arestas_3d


def main(outdir="resultados"):
    print("=" * 60)
    print("2) MODELAGEM E TRANSFORMACAO 3D (CUBO)")
    print("=" * 60)

    vertices = cubo_vertices(lado=2.0)
    theta = 40
    translacao = (2.0, 1.0, 0.5)
    M = matriz_transformacao_3d(theta, translacao)
    vertices_transf = aplicar_transformacao_3d(M, vertices)

    print(f"Vertices originais:\n{vertices}")
    print(f"Angulo de rotacao (eixo Z): {theta} graus")
    print(f"Translacao: {translacao}")
    print(f"Matriz de transformacao homogenea M =\n{np.round(M, 4)}")
    print(f"Vertices transformados:\n{np.round(vertices_transf, 4)}")

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")
    plotar_arestas_3d(ax, vertices, ARESTAS_CUBO, "tab:blue", label="antes")
    plotar_arestas_3d(ax, vertices_transf, ARESTAS_CUBO, "tab:red", label="depois")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(f"Cubo: rotacao de {theta} graus em Z + translacao {translacao}")
    ax.legend()

    plt.tight_layout()
    fig.savefig(f"{outdir}/02_transformacao_3d.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/02_transformacao_3d.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
