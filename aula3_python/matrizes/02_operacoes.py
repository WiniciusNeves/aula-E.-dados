"""
2) Operacoes com matrizes: soma, subtracao, multiplicacao (matricial e
elemento a elemento) e multiplicacao por escalar.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import mostrar_matriz


def main(outdir="resultados"):
    print("=" * 60)
    print("2) OPERACOES COM MATRIZES")
    print("=" * 60)

    A = np.array([[2, 3], [1, 0]])
    B = np.array([[3, 1], [-1, -2]])
    c = 2

    soma = A + B
    subtracao = A - B
    mult_matricial = A @ B
    mult_elemento = A * B
    escalar = c * A

    print(f"A =\n{A}")
    print(f"B =\n{B}")
    print(f"\nA + B =\n{soma}")
    print(f"\nA - B =\n{subtracao}")
    print(f"\nA @ B (multiplicacao matricial) =\n{mult_matricial}")
    print(f"\nA * B (elemento a elemento) =\n{mult_elemento}")
    print(f"\n{c}.A (multiplicacao por escalar) =\n{escalar}")

    fig, axs = plt.subplots(2, 3, figsize=(12, 8))
    mostrar_matriz(axs[0, 0], A, "A")
    mostrar_matriz(axs[0, 1], B, "B")
    mostrar_matriz(axs[0, 2], soma, "A + B")
    mostrar_matriz(axs[1, 0], subtracao, "A - B")
    mostrar_matriz(axs[1, 1], mult_matricial, "A @ B")
    mostrar_matriz(axs[1, 2], escalar, f"{c}.A")

    plt.tight_layout()
    fig.savefig(f"{outdir}/02_operacoes.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/02_operacoes.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
