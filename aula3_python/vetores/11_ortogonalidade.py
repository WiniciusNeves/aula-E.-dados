"""
11) Ortogonalidade de vetores: u e v sao ortogonais quando u . v = 0.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import vt


def main(outdir="resultados"):
    print("=" * 60)
    print("11) ORTOGONALIDADE DE VETORES")
    print("=" * 60)
    print("Dois vetores u e v sao ortogonais (perpendiculares) se e somente")
    print("se u . v = 0.")
    print()

    u = np.array([3, 2])
    v_ortogonal = np.array([-2, 3])   # perpendicular a u
    v_nao_ortogonal = np.array([1, 1])

    dot_ortogonal = np.dot(u, v_ortogonal)
    dot_nao = np.dot(u, v_nao_ortogonal)

    print(f"u = {vt(u)}")
    print(f"v1 = {vt(v_ortogonal)}   u.v1 = {dot_ortogonal}   -> {'ORTOGONAIS' if np.isclose(dot_ortogonal, 0) else 'NAO ORTOGONAIS'}")
    print(f"v2 = {vt(v_nao_ortogonal)}   u.v2 = {dot_nao}   -> {'ORTOGONAIS' if np.isclose(dot_nao, 0) else 'NAO ORTOGONAIS'}")

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    def desenhar(ax, v1, v2, produto, titulo):
        ax.quiver(0, 0, v1[0], v1[1], angles="xy", scale_units="xy", scale=1, color="tab:blue", label="u")
        ax.quiver(0, 0, v2[0], v2[1], angles="xy", scale_units="xy", scale=1, color="tab:orange", label="v")
        limite = max(abs(v1).max(), abs(v2).max()) + 1
        ax.set_xlim(-limite, limite)
        ax.set_ylim(-limite, limite)
        ax.set_aspect("equal")
        ax.grid(True)
        ax.axhline(0, color="black", linewidth=0.5)
        ax.axvline(0, color="black", linewidth=0.5)
        ax.set_title(f"{titulo}\nu.v = {produto}")
        ax.legend()

    desenhar(axs[0], u, v_ortogonal, dot_ortogonal, "Vetores ortogonais")
    desenhar(axs[1], u, v_nao_ortogonal, dot_nao, "Vetores nao ortogonais")

    plt.tight_layout()
    fig.savefig(f"{outdir}/11_ortogonalidade.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/11_ortogonalidade.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
