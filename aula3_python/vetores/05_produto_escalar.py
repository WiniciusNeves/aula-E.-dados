"""
5) Produto escalar (dot product) entre dois vetores e o angulo entre eles.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

from _util import vt


def main(outdir="resultados"):
    print("=" * 60)
    print("5) PRODUTO ESCALAR (DOT PRODUCT)")
    print("=" * 60)

    u = np.array([3, 1])
    v = np.array([1, 3])

    produto_escalar = np.dot(u, v)
    norma_u = np.linalg.norm(u)
    norma_v = np.linalg.norm(v)
    cos_theta = produto_escalar / (norma_u * norma_v)
    theta_graus = np.degrees(np.arccos(np.clip(cos_theta, -1, 1)))

    print(f"u = {vt(u)}")
    print(f"v = {vt(v)}")
    print(f"u . v = {produto_escalar}")
    print(f"|u| = {norma_u:.4f}   |v| = {norma_v:.4f}")
    print(f"cos(theta) = {cos_theta:.4f}")
    print(f"Angulo entre u e v = {theta_graus:.2f} graus")

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.quiver(0, 0, u[0], u[1], angles="xy", scale_units="xy", scale=1, color="tab:blue", label="u")
    ax.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1, color="tab:orange", label="v")
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ang_u = np.degrees(np.arctan2(u[1], u[0]))
    ang_v = np.degrees(np.arctan2(v[1], v[0]))
    arco = Arc((0, 0), 1.5, 1.5, angle=0, theta1=min(ang_u, ang_v), theta2=max(ang_u, ang_v), color="tab:green")
    ax.add_patch(arco)
    ax.set_title(f"u.v = {produto_escalar}   |   angulo = {theta_graus:.1f} graus")
    ax.legend()

    plt.tight_layout()
    fig.savefig(f"{outdir}/05_produto_escalar.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/05_produto_escalar.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
