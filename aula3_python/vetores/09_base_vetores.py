"""
9) Base de um espaco vetorial: o conjunto minimo de vetores LI que gera todo
o espaco. Em TI, a Base Canonica e o padrao (vetores unitarios [1,0,0], etc).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import vt


def main(outdir="resultados"):
    print("=" * 60)
    print("9) BASE DE VETORES (conjunto minimo que gera o espaco)")
    print("=" * 60)

    # Base canonica do R2
    e1 = np.array([1, 0])
    e2 = np.array([0, 1])
    v = np.array([3, 2])

    print("Base canonica do R2: {e1, e2} = {(1,0), (0,1)}")
    print(f"Exemplo: v = {vt(v)} = {v[0]}.e1 + {v[1]}.e2")

    # Base canonica do R3
    i3 = np.array([1, 0, 0])
    j3 = np.array([0, 1, 0])
    k3 = np.array([0, 0, 1])
    w = np.array([2, -1, 3])
    print()
    print("Base canonica do R3: {i, j, k} = {(1,0,0), (0,1,0), (0,0,1)}")
    print(f"Exemplo: w = {vt(w)} = {w[0]}.i + {w[1]}.j + {w[2]}.k")

    # Base alternativa (nao canonica) do R2
    b1 = np.array([1, 1])
    b2 = np.array([1, -1])
    matriz_base = np.array([b1, b2]).T
    coeficientes = np.linalg.solve(matriz_base, v)
    print()
    print("Base alternativa (nao canonica) do R2: {b1, b2} = {(1,1), (1,-1)}")
    print(f"  v = {coeficientes[0]:.2f}.b1 + {coeficientes[1]:.2f}.b2")

    fig = plt.figure(figsize=(15, 5))

    ax1 = fig.add_subplot(1, 3, 1)
    ax1.quiver(0, 0, e1[0], e1[1], angles="xy", scale_units="xy", scale=1, color="tab:blue", label="e1")
    ax1.quiver(0, 0, e2[0], e2[1], angles="xy", scale_units="xy", scale=1, color="tab:orange", label="e2")
    ax1.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1, color="tab:green", label="v")
    ax1.set_xlim(-1, 4)
    ax1.set_ylim(-1, 3)
    ax1.set_aspect("equal")
    ax1.grid(True)
    ax1.axhline(0, color="black", linewidth=0.5)
    ax1.axvline(0, color="black", linewidth=0.5)
    ax1.set_title("Base canonica {e1, e2} do R2")
    ax1.legend()

    ax2 = fig.add_subplot(1, 3, 2)
    ax2.quiver(0, 0, b1[0], b1[1], angles="xy", scale_units="xy", scale=1, color="tab:blue", label="b1")
    ax2.quiver(0, 0, b2[0], b2[1], angles="xy", scale_units="xy", scale=1, color="tab:orange", label="b2")
    ax2.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1, color="tab:green", label="v")
    ax2.set_xlim(-2, 4)
    ax2.set_ylim(-2, 3)
    ax2.set_aspect("equal")
    ax2.grid(True)
    ax2.axhline(0, color="black", linewidth=0.5)
    ax2.axvline(0, color="black", linewidth=0.5)
    ax2.set_title("Base alternativa {b1, b2} do R2")
    ax2.legend()

    ax3 = fig.add_subplot(1, 3, 3, projection="3d")
    ax3.quiver(0, 0, 0, *i3, color="tab:blue", label="i")
    ax3.quiver(0, 0, 0, *j3, color="tab:orange", label="j")
    ax3.quiver(0, 0, 0, *k3, color="tab:red", label="k")
    ax3.quiver(0, 0, 0, *w, color="tab:green", label="w")
    ax3.set_xlim(0, 3)
    ax3.set_ylim(-2, 1)
    ax3.set_zlim(0, 4)
    ax3.set_title("Base canonica {i, j, k} do R3")
    ax3.legend()

    plt.tight_layout()
    fig.savefig(f"{outdir}/09_base_vetores.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/09_base_vetores.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
