"""Funcoes auxiliares compartilhadas pelos scripts do modulo Rasterizacao e Shading."""
import numpy as np


def bresenham(x0, y0, x1, y1):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    pontos = []
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    erro = dx + dy
    x, y = x0, y0
    while True:
        pontos.append((x, y))
        if x == x1 and y == y1:
            break
        e2 = 2 * erro
        if e2 >= dy:
            erro += dy
            x += sx
        if e2 <= dx:
            erro += dx
            y += sy
    return pontos


def borda(a, b, p):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])


def rasterizar_triangulo(v0, v1, v2, altura, largura, cores):
    xs = (v0[0], v1[0], v2[0])
    ys = (v0[1], v1[1], v2[1])
    xmin = max(int(np.floor(min(xs))), 0)
    xmax = min(int(np.ceil(max(xs))), largura - 1)
    ymin = max(int(np.floor(min(ys))), 0)
    ymax = min(int(np.ceil(max(ys))), altura - 1)

    imagem = np.zeros((altura, largura, 3))
    area = borda(v0, v1, v2)
    c0, c1, c2 = cores

    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            p = (x + 0.5, y + 0.5)
            w0 = borda(v1, v2, p) / area
            w1 = borda(v2, v0, p) / area
            w2 = borda(v0, v1, p) / area
            dentro = (w0 >= 0 and w1 >= 0 and w2 >= 0) or (w0 <= 0 and w1 <= 0 and w2 <= 0)
            if dentro:
                imagem[y, x] = w0 * c0 + w1 * c1 + w2 * c2

    return imagem
