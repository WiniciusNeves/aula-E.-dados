"""
10) Propriedades de soma e multiplicacao de vetores: comutativa, elemento
oposto, associativa, elemento neutro.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import vt


def main(outdir="resultados"):
    print("=" * 60)
    print("10) PROPRIEDADES DE SOMA E MULTIPLICACAO DE VETORES")
    print("=" * 60)

    u = np.array([2, 1])
    v = np.array([1, 3])
    w = np.array([-1, 2])
    zero = np.array([0, 0])

    # (a) comutativa
    comutativa_ok = np.allclose(u + v, v + u)
    print(f"(a) Comutativa:  u+v = {vt(u+v)}   v+u = {vt(v+u)}   -> {'OK' if comutativa_ok else 'FALHOU'}")

    # (b) elemento oposto
    oposto_ok = np.allclose(u + (-u), zero)
    print(f"(b) Elemento oposto:  u+(-u) = {vt(u+(-u))}   -> {'OK' if oposto_ok else 'FALHOU'}")

    # (c) associativa
    associativa_ok = np.allclose((u + v) + w, u + (v + w))
    print(f"(c) Associativa:  (u+v)+w = {vt((u+v)+w)}   u+(v+w) = {vt(u+(v+w))}   -> {'OK' if associativa_ok else 'FALHOU'}")

    # (d) elemento neutro
    neutro_ok = np.allclose(u + zero, u)
    print(f"(d) Elemento neutro:  u+0 = {vt(u+zero)}   -> {'OK' if neutro_ok else 'FALHOU'}")

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    def desenhar(ax, vetores, titulo):
        cores = ["tab:blue", "tab:orange", "tab:green", "tab:red"]
        limite = max(abs(vet).max() for vet, _ in vetores) + 1
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

    desenhar(axs[0], [(u, "u"), (v, "v"), (u + v, "u+v = v+u")], "Comutativa: u+v = v+u")
    desenhar(axs[1], [(u, "u"), (-u, "-u")], "Elemento oposto: u + (-u) = 0")

    plt.tight_layout()
    fig.savefig(f"{outdir}/10_propriedades.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/10_propriedades.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
