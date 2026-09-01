"""
2) Vetores no espaco vetorial 2D e 3D.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import vt


def main(outdir="resultados"):
    print("=" * 60)
    print("2) VETORES NO ESPACO VETORIAL 2D E 3D")
    print("=" * 60)

    v2d = np.array([3, 4])
    v3d = np.array([2, -1, 3])

    print(f"Vetor v (R2)  = {vt(v2d)}  -> nomenclatura: v = (x, y)")
    print(f"Vetor w (R3)  = {vt(v3d)}  -> nomenclatura: w = (x, y, z)")
    print()
    print("Vetores unitarios (versores) usados para nomear componentes:")
    print("  R2: i = (1, 0), j = (0, 1)          -> v = x.i + y.j")
    print("  R3: i = (1, 0, 0), j = (0, 1, 0), k = (0, 0, 1) -> w = x.i + y.j + z.k")

    fig = plt.figure(figsize=(11, 5))

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.quiver(0, 0, v2d[0], v2d[1], angles="xy", scale_units="xy", scale=1, color="tab:blue")
    ax1.set_xlim(-1, 5)
    ax1.set_ylim(-1, 5)
    ax1.set_aspect("equal")
    ax1.grid(True)
    ax1.axhline(0, color="black", linewidth=0.5)
    ax1.axvline(0, color="black", linewidth=0.5)
    ax1.set_title(f"Vetor em R2: v = {vt(v2d)}")

    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    ax2.quiver(0, 0, 0, v3d[0], v3d[1], v3d[2], color="tab:red")
    ax2.set_xlim(0, 3)
    ax2.set_ylim(-2, 1)
    ax2.set_zlim(0, 4)
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_zlabel("z")
    ax2.set_title(f"Vetor em R3: w = {vt(v3d)}")

    plt.tight_layout()
    fig.savefig(f"{outdir}/02_vetores_2d_3d.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/02_vetores_2d_3d.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
