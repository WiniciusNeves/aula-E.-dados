"""Funcoes auxiliares compartilhadas pelos scripts do modulo Modelagem 2D/3D."""
import numpy as np


def cubo_vertices(lado=1.0):
    l = lado / 2
    return np.array([
        [-l, -l, -l],
        [l, -l, -l],
        [l, l, -l],
        [-l, l, -l],
        [-l, -l, l],
        [l, -l, l],
        [l, l, l],
        [-l, l, l],
    ])


ARESTAS_CUBO = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]


def matriz_transformacao_3d(theta_graus, translacao):
    t = np.radians(theta_graus)
    tx, ty, tz = translacao
    return np.array([
        [np.cos(t), -np.sin(t), 0, tx],
        [np.sin(t), np.cos(t), 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1],
    ])


def aplicar_transformacao_3d(M, vertices):
    n = vertices.shape[0]
    homogeneos = np.hstack([vertices, np.ones((n, 1))])
    transformados = (M @ homogeneos.T).T
    return transformados[:, :3]


def plotar_arestas_3d(ax, vertices, arestas, cor, label=None):
    for i, (a, b) in enumerate(arestas):
        p1, p2 = vertices[a], vertices[b]
        ax.plot(
            [p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]],
            color=cor, marker="o", label=label if i == 0 else None,
        )
