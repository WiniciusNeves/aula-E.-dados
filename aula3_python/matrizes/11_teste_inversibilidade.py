"""
11) Teste para saber se uma matriz e inversivel (nao singular): det(A) != 0.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import mostrar_matriz


def eh_inversivel(A):
    return not np.isclose(np.linalg.det(A), 0)


def main(outdir="resultados"):
    print("=" * 60)
    print("11) TESTE DE INVERSIBILIDADE (det(A) != 0)")
    print("=" * 60)

    A_inversivel = np.array([
        [2, 0, 1, 0],
        [1, 3, 0, 1],
        [0, 1, 4, 2],
        [1, 0, 1, 5],
    ], dtype=float)

    # matriz singular: 4a linha = combinacao das duas primeiras
    A_singular = np.array([
        [1, 2, 0, 1],
        [0, 1, 1, 2],
        [2, 4, 0, 2],   # = 2 * linha 1 -> torna a matriz singular
        [1, 1, 1, 1],
    ], dtype=float)

    for nome, A in [("A (esperado: inversivel)", A_inversivel), ("B (esperado: singular)", A_singular)]:
        det = np.linalg.det(A)
        print(f"{nome} =\n{A}")
        print(f"  det = {det:.6f}   -> {'INVERSIVEL (nao singular)' if eh_inversivel(A) else 'SINGULAR (nao inversivel)'}\n")

    fig, axs = plt.subplots(1, 2, figsize=(9, 4.5))
    mostrar_matriz(axs[0], A_inversivel, f"det = {np.linalg.det(A_inversivel):.2f} -> inversivel")
    mostrar_matriz(axs[1], A_singular, f"det = {np.linalg.det(A_singular):.2f} -> singular")
    plt.tight_layout()
    fig.savefig(f"{outdir}/11_teste_inversibilidade.png", dpi=150)
    plt.close(fig)
    print(f"Grafico salvo em: {outdir}/11_teste_inversibilidade.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
