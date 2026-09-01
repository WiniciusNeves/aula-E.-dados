"""
4) Tipos especiais de matrizes: nula, linha, coluna, quadrada, retangular,
diagonal, identidade, triangular inferior, triangular superior, simetrica.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import mostrar_matriz


def eh_nula(A):
    return np.all(A == 0)


def eh_linha(A):
    return A.shape[0] == 1


def eh_coluna(A):
    return A.shape[1] == 1


def eh_quadrada(A):
    return A.shape[0] == A.shape[1]


def eh_retangular(A):
    return A.shape[0] != A.shape[1]


def eh_diagonal(A):
    return eh_quadrada(A) and np.all(A - np.diag(np.diagonal(A)) == 0)


def eh_identidade(A):
    return eh_diagonal(A) and np.all(np.diagonal(A) == 1)


def eh_triangular_inferior(A):
    return eh_quadrada(A) and np.allclose(A, np.tril(A))


def eh_triangular_superior(A):
    return eh_quadrada(A) and np.allclose(A, np.triu(A))


def eh_simetrica(A):
    return eh_quadrada(A) and np.allclose(A, A.T)


def main(outdir="resultados"):
    print("=" * 60)
    print("4) TIPOS ESPECIAIS DE MATRIZES")
    print("=" * 60)

    exemplos = {
        "Nula": (np.zeros((2, 3)), eh_nula),
        "Linha": (np.array([[1, 2, 3]]), eh_linha),
        "Coluna": (np.array([[1], [2], [3]]), eh_coluna),
        "Quadrada": (np.array([[1, 2], [3, 4]]), eh_quadrada),
        "Retangular": (np.array([[1, 2, 3], [4, 5, 6]]), eh_retangular),
        "Diagonal": (np.diag([2, 5, 7]), eh_diagonal),
        "Identidade": (np.eye(3), eh_identidade),
        "Triangular inferior": (np.array([[1, 0, 0], [2, 3, 0], [4, 5, 6]]), eh_triangular_inferior),
        "Triangular superior": (np.array([[1, 2, 3], [0, 4, 5], [0, 0, 6]]), eh_triangular_superior),
        "Simetrica": (np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6]]), eh_simetrica),
    }

    for nome, (matriz, verificador) in exemplos.items():
        print(f"{nome}:\n{matriz}\n  -> verificacao: {verificador(matriz)}\n")

    fig, axs = plt.subplots(2, 5, figsize=(20, 8))
    for ax, (nome, (matriz, _)) in zip(axs.flat, exemplos.items()):
        mostrar_matriz(ax, matriz, nome, destacar_diagonal=True)

    plt.tight_layout()
    fig.savefig(f"{outdir}/04_tipos_especiais.png", dpi=150)
    plt.close(fig)
    print(f"Grafico salvo em: {outdir}/04_tipos_especiais.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
