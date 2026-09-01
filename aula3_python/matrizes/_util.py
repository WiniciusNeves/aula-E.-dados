"""Funcoes auxiliares compartilhadas pelos scripts do modulo Matrizes."""
import numpy as np
import matplotlib.pyplot as plt


def mostrar_matriz(ax, matriz, titulo, cmap="Blues", destacar_diagonal=False):
    """Desenha uma matriz como heatmap com os valores anotados em cada celula."""
    matriz = np.asarray(matriz, dtype=float)
    ax.imshow(matriz, cmap=cmap, vmin=matriz.min() - 1, vmax=matriz.max() + 1)
    for (i, j), valor in np.ndenumerate(matriz):
        cor_texto = "black"
        peso = "bold" if destacar_diagonal and i == j else "normal"
        ax.text(j, i, f"{valor:g}", ha="center", va="center", color=cor_texto, fontweight=peso)
    ax.set_xticks(range(matriz.shape[1]))
    ax.set_yticks(range(matriz.shape[0]))
    ax.set_title(titulo)
