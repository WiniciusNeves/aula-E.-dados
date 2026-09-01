"""
4) Norma (modulo) de um vetor em 2D e 3D.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import vt


def main(outdir="resultados"):
    print("=" * 60)
    print("4) NORMA DO VETOR (2D E 3D)")
    print("=" * 60)
    print("A norma de v = (x1, ..., xn) e definida por:")
    print("    |v| = sqrt(x1^2 + x2^2 + ... + xn^2)")
    print()

    v2d = np.array([3.0, 4.0])
    v3d = np.array([1.0, 2.0, 2.0])

    norma_2d = np.linalg.norm(v2d)
    norma_3d = np.linalg.norm(v3d)
    unitario_2d = v2d / norma_2d
    unitario_3d = v3d / norma_3d

    print(f"v (R2) = {vt(v2d)}   |v| = {norma_2d:.4f}")
    print(f"  vetor unitario (versor) na direcao de v: {vt(unitario_2d)}")
    print()
    print(f"w (R3) = {vt(v3d)}   |w| = {norma_3d:.4f}")
    print(f"  vetor unitario (versor) na direcao de w: {vt(unitario_3d)}")

    fig = plt.figure(figsize=(11, 5))

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.quiver(0, 0, v2d[0], v2d[1], angles="xy", scale_units="xy", scale=1, color="tab:blue", label=f"v, |v|={norma_2d:.2f}")
    ax1.quiver(0, 0, unitario_2d[0], unitario_2d[1], angles="xy", scale_units="xy", scale=1, color="tab:green", label="versor de v")
    ax1.set_xlim(-1, 5)
    ax1.set_ylim(-1, 5)
    ax1.set_aspect("equal")
    ax1.grid(True)
    ax1.axhline(0, color="black", linewidth=0.5)
    ax1.axvline(0, color="black", linewidth=0.5)
    ax1.legend()
    ax1.set_title(f"Norma em R2: |v| = {norma_2d:.4f}")

    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    ax2.quiver(0, 0, 0, *v3d, color="tab:blue", label=f"w, |w|={norma_3d:.2f}")
    ax2.quiver(0, 0, 0, *unitario_3d, color="tab:green", label="versor de w")
    ax2.set_xlim(0, 2)
    ax2.set_ylim(0, 2)
    ax2.set_zlim(0, 2)
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_zlabel("z")
    ax2.legend()
    ax2.set_title(f"Norma em R3: |w| = {norma_3d:.4f}")

    plt.tight_layout()
    fig.savefig(f"{outdir}/04_norma.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/04_norma.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
