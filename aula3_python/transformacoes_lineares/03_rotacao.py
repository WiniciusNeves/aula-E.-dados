"""
3) Rotacao: girar o espaco em torno da origem por um angulo theta.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import quadrado_unitario, aplicar_transformacao, plotar_antes_depois


def main(outdir="resultados"):
    print("=" * 60)
    print("3) ROTACAO")
    print("=" * 60)

    theta = 45
    theta_rad = np.radians(theta)
    M_rotacao = np.array([
        [np.cos(theta_rad), -np.sin(theta_rad)],
        [np.sin(theta_rad), np.cos(theta_rad)],
    ])

    print(f"Angulo de rotacao: {theta} graus")
    print(f"Matriz de rotacao M =\n{np.round(M_rotacao, 4)}")

    antes = quadrado_unitario()
    depois = aplicar_transformacao(M_rotacao, antes)

    fig, ax = plt.subplots(figsize=(5, 5))
    plotar_antes_depois(ax, antes, depois, f"Rotacao de {theta} graus (sentido anti-horario)")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    plt.tight_layout()
    fig.savefig(f"{outdir}/03_rotacao.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/03_rotacao.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
