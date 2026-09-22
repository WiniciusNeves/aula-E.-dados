"""
1) Pontos em coordenadas cartesianas 2D e campo vetorial com plt.scatter/plt.quiver.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main(outdir="resultados"):
    print("=" * 60)
    print("1) PONTOS E CAMPO VETORIAL 2D")
    print("=" * 60)

    pontos = np.array([
        [1, 1],
        [2, 4],
        [4, 2],
        [5, 5],
        [0, 3],
        [3, 0],
    ])
    cores_pontos = ["tab:blue", "tab:orange", "tab:green", "tab:purple", "tab:brown", "tab:cyan"]
    alvo = np.array([3, 3])

    dx = alvo[0] - pontos[:, 0]
    dy = alvo[1] - pontos[:, 1]

    print(f"Pontos:\n{pontos}")
    print(f"Alvo (origem do campo de atracao): {tuple(alvo)}")
    print(f"Vetores (dx, dy) ate o alvo:\n{np.column_stack([dx, dy])}")

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(pontos[:, 0], pontos[:, 1], color=cores_pontos, s=90, zorder=3, label="pontos")
    ax.scatter(*alvo, color="black", marker="*", s=250, zorder=3, label="alvo")
    ax.quiver(
        pontos[:, 0], pontos[:, 1], dx, dy,
        color="tab:red", angles="xy", scale_units="xy", scale=1,
    )
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 6)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.set_title("Pontos 2D e campo vetorial convergindo para o alvo")
    ax.legend()

    plt.tight_layout()
    fig.savefig(f"{outdir}/01_pontos_vetores_2d.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/01_pontos_vetores_2d.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
