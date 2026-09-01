"""Funcoes auxiliares compartilhadas pelos scripts do modulo Transformacao Linear."""
import numpy as np


def quadrado_unitario():
    """Retorna os vertices de um quadrado unitario (para visualizar transformacoes)."""
    return np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T  # 2 x 5 (fechado)


def aplicar_transformacao(M, pontos):
    """Aplica a matriz M (2x2) a um conjunto de pontos (2 x n)."""
    return M @ pontos


def plotar_antes_depois(ax, antes, depois, titulo):
    ax.plot(antes[0], antes[1], "o-", color="tab:blue", label="antes")
    ax.plot(depois[0], depois[1], "o-", color="tab:red", label="depois")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.grid(True)
    ax.set_aspect("equal")
    ax.legend()
    ax.set_title(titulo)
