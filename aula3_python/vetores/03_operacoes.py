"""
3) Operacoes com vetores: soma, subtracao, multiplicacao e divisao
(elemento a elemento) e multiplicacao por escalar.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import vt


def main(outdir="resultados"):
    print("=" * 60)
    print("3) OPERACOES COM VETORES")
    print("=" * 60)

    u = np.array([2.0, 3.0])
    v = np.array([4.0, -1.0])

    soma = u + v
    subtracao = u - v
    mult_elemento = u * v          # multiplicacao elemento a elemento (Hadamard)
    divisao_elemento = u / v       # divisao elemento a elemento
    escalar = 2 * u

    print(f"u = {vt(u)}")
    print(f"v = {vt(v)}")
    print(f"u + v (soma)                       = {vt(soma)}")
    print(f"u - v (subtracao)                  = {vt(subtracao)}")
    print(f"u * v (mult. elemento a elemento)  = {vt(mult_elemento)}")
    print(f"u / v (div. elemento a elemento)   = {vt(divisao_elemento)}")
    print(f"2.u (multiplicacao por escalar)    = {vt(escalar)}")

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    def desenhar(ax, lista_vetores, titulo):
        cores = ["tab:blue", "tab:orange", "tab:green"]
        limite = max(abs(vet).max() for vet, _ in lista_vetores) + 1
        for (vet, nome), cor in zip(lista_vetores, cores):
            ax.quiver(0, 0, vet[0], vet[1], angles="xy", scale_units="xy", scale=1, color=cor, label=nome)
        ax.set_xlim(-limite, limite)
        ax.set_ylim(-limite, limite)
        ax.set_aspect("equal")
        ax.grid(True)
        ax.axhline(0, color="black", linewidth=0.5)
        ax.axvline(0, color="black", linewidth=0.5)
        ax.legend()
        ax.set_title(titulo)

    desenhar(axs[0], [(u, "u"), (v, "v"), (soma, "u+v")], "Soma (regra do paralelogramo)")
    desenhar(axs[1], [(u, "u"), (v, "v"), (subtracao, "u-v")], "Subtracao")
    desenhar(axs[2], [(u, "u"), (escalar, "2.u")], "Multiplicacao por escalar")

    plt.tight_layout()
    fig.savefig(f"{outdir}/03_operacoes.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/03_operacoes.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
