"""
2) Expansao/Contracao (Scaling): esticar ou encolher o espaco.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import quadrado_unitario, aplicar_transformacao, plotar_antes_depois


def main(outdir="resultados"):
    print("=" * 60)
    print("2) EXPANSAO/CONTRACAO (SCALING)")
    print("=" * 60)

    sx, sy = 2, 0.5
    M_escala = np.array([[sx, 0], [0, sy]])

    print(f"Matriz de escala M =\n{M_escala}")
    print(f"  sx = {sx} (expande no eixo x)")
    print(f"  sy = {sy} (contrai no eixo y)")

    antes = quadrado_unitario()
    depois = aplicar_transformacao(M_escala, antes)

    fig, ax = plt.subplots(figsize=(5, 5))
    plotar_antes_depois(ax, antes, depois, f"Escala: sx={sx} (expande), sy={sy} (contrai)")
    plt.tight_layout()
    fig.savefig(f"{outdir}/02_escala.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/02_escala.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
