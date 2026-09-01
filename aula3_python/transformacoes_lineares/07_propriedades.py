"""
7) Propriedades de uma transformacao linear T(x) = A.x:
a) T(u+v) = T(u) + T(v)        (aditividade)
b) T(alpha.u) = alpha.T(u)     (homogeneidade)
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def vt(v):
    return tuple(np.round(np.asarray(v, dtype=float), 4).tolist())



def main(outdir="resultados"):
    print("=" * 60)
    print("7) PROPRIEDADES DE TRANSFORMACAO LINEAR")
    print("=" * 60)

    A = np.array([[2, 1], [0, 3]])

    def T(x):
        return A @ x

    u = np.array([1.0, 2.0])
    v = np.array([3.0, -1.0])
    alpha = 2.5

    a_ok = np.allclose(T(u + v), T(u) + T(v))
    b_ok = np.allclose(T(alpha * u), alpha * T(u))

    print(f"A =\n{A}")
    print(f"u = {vt(u)}   v = {vt(v)}   alpha = {alpha}")
    print()
    print(f"a) T(u+v) = {vt(T(u+v))}   T(u)+T(v) = {vt(T(u)+T(v))}   -> {'OK' if a_ok else 'FALHOU'}")
    print(f"b) T(alpha.u) = {vt(T(alpha*u))}   alpha.T(u) = {vt(alpha*T(u))}   -> {'OK' if b_ok else 'FALHOU'}")

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    def desenhar(ax, vetores, titulo):
        cores = ["tab:blue", "tab:orange", "tab:green"]
        limite = max(abs(vet).max() for vet, _ in vetores) + 2
        for (vet, nome), cor in zip(vetores, cores):
            ax.quiver(0, 0, vet[0], vet[1], angles="xy", scale_units="xy", scale=1, color=cor, label=nome)
        ax.set_xlim(-limite, limite)
        ax.set_ylim(-limite, limite)
        ax.set_aspect("equal")
        ax.grid(True)
        ax.axhline(0, color="black", linewidth=0.5)
        ax.axvline(0, color="black", linewidth=0.5)
        ax.legend()
        ax.set_title(titulo)

    desenhar(axs[0], [(T(u), "T(u)"), (T(v), "T(v)"), (T(u + v), "T(u+v)")], "Aditividade: T(u+v)=T(u)+T(v)")
    desenhar(axs[1], [(T(u), "T(u)"), (T(alpha * u), "T(alpha.u)")], "Homogeneidade: T(alpha.u)=alpha.T(u)")

    plt.tight_layout()
    fig.savefig(f"{outdir}/07_propriedades.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/07_propriedades.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
