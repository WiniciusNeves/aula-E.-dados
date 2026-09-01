"""
6) Produto vetorial (cross product) entre dois vetores em R3.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import vt


def main(outdir="resultados"):
    print("=" * 60)
    print("6) PRODUTO VETORIAL (CROSS PRODUCT)")
    print("=" * 60)

    u = np.array([2, 0, 0])
    v = np.array([0, 2, 0])

    produto_vetorial = np.cross(u, v)

    print(f"u = {vt(u)}")
    print(f"v = {vt(v)}")
    print(f"u x v = {vt(produto_vetorial)}")
    print(f"(u x v) . u = {np.dot(produto_vetorial, u)}  (perpendicular a u)")
    print(f"(u x v) . v = {np.dot(produto_vetorial, v)}  (perpendicular a v)")
    print(f"|u x v| = {np.linalg.norm(produto_vetorial):.4f}  (area do paralelogramo formado por u e v)")

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(projection="3d")
    ax.quiver(0, 0, 0, *u, color="tab:blue", label="u")
    ax.quiver(0, 0, 0, *v, color="tab:orange", label="v")
    ax.quiver(0, 0, 0, *produto_vetorial, color="tab:green", label="u x v")
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_zlim(0, 5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("Produto vetorial: u x v e perpendicular a u e a v")
    ax.legend()

    plt.tight_layout()
    fig.savefig(f"{outdir}/06_produto_vetorial.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/06_produto_vetorial.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
