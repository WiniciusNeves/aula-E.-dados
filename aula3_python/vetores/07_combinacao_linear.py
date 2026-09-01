"""
7) Combinacao linear de vetores: w = a.v + b.u
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import vt


def main(outdir="resultados"):
    print("=" * 60)
    print("7) COMBINACAO LINEAR: w = a.v + b.u")
    print("=" * 60)

    v = np.array([1, 0])
    u = np.array([0, 1])
    a, b = 3, 2

    w = a * v + b * u

    print(f"v = {vt(v)}   u = {vt(u)}")
    print(f"escalares: a = {a}, b = {b}")
    print(f"w = a.v + b.u = {a}.{vt(v)} + {b}.{vt(u)} = {vt(w)}")

    fig, ax = plt.subplots(figsize=(6, 6))
    origem = np.array([0, 0])
    av = a * v
    ax.quiver(*origem, *av, angles="xy", scale_units="xy", scale=1, color="tab:blue", label=f"{a}.v")
    ax.quiver(*av, *(b * u), angles="xy", scale_units="xy", scale=1, color="tab:orange", label=f"{b}.u")
    ax.quiver(*origem, *w, angles="xy", scale_units="xy", scale=1, color="tab:green", label="w = a.v+b.u")
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 3)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.set_title(f"Combinacao linear: w = {vt(w)}")
    ax.legend()

    plt.tight_layout()
    fig.savefig(f"{outdir}/07_combinacao_linear.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/07_combinacao_linear.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
