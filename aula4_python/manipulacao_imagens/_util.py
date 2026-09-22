"""Funcoes auxiliares compartilhadas pelos scripts do modulo Manipulacao de Imagens."""
import os
import numpy as np
from PIL import Image


def gerar_imagem_exemplo(caminho="imagem_exemplo.png", altura=120, largura=160):
    if os.path.exists(caminho):
        return caminho

    y = np.linspace(0, 1, altura).reshape(-1, 1)
    ceu_r = 0.53 - 0.25 * y
    ceu_g = 0.75 - 0.20 * y
    ceu_b = 0.95 - 0.10 * y
    imagem = np.stack([
        np.tile(ceu_r, (1, largura)),
        np.tile(ceu_g, (1, largura)),
        np.tile(ceu_b, (1, largura)),
    ], axis=-1)

    linha_horizonte = int(altura * 0.55)
    imagem[linha_horizonte:, :, :] = [0.95, 0.95, 0.98]

    xx, yy = np.meshgrid(np.arange(largura), np.arange(altura))

    sol = (xx - int(largura * 0.15)) ** 2 + (yy - int(altura * 0.15)) ** 2 <= 12 ** 2
    imagem[sol] = [1.0, 0.85, 0.2]

    y0, y1 = linha_horizonte + 18, linha_horizonte + 32
    x0, x1 = int(largura * 0.35), int(largura * 0.65)
    imagem[y0:y1, x0:x1] = [0.75, 0.10, 0.10]

    for cx in (int(largura * 0.12), int(largura * 0.85)):
        base_y = linha_horizonte
        altura_arvore = 22
        for i in range(altura_arvore):
            largura_linha = int((altura_arvore - i) * 0.35) + 1
            ly = base_y - i
            lx0, lx1 = cx - largura_linha, cx + largura_linha
            imagem[ly, lx0:lx1] = [0.10, 0.35, 0.15]

    imagem_uint8 = (np.clip(imagem, 0, 1) * 255).astype(np.uint8)
    Image.fromarray(imagem_uint8).save(caminho)
    return caminho


def carregar_imagem_normalizada(caminho):
    imagem_pil = Image.open(caminho).convert("RGB")
    array = np.asarray(imagem_pil).astype(np.float64)
    return array / 255.0
