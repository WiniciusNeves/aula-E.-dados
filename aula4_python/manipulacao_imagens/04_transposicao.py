"""
4) Transposicao de matrizes (np.transpose) aplicada a cada canal de cor e reconstrucao da imagem.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import gerar_imagem_exemplo, carregar_imagem_normalizada


def main(outdir="resultados"):
    print("=" * 60)
    print("4) TRANSPOSICAO DE MATRIZES POR CANAL")
    print("=" * 60)

    caminho = gerar_imagem_exemplo()
    original = carregar_imagem_normalizada(caminho)

    r, g, b = original[:, :, 0], original[:, :, 1], original[:, :, 2]
    r_t, g_t, b_t = np.transpose(r), np.transpose(g), np.transpose(b)
    transposta = np.stack([r_t, g_t, b_t], axis=-1)

    print(f"Formato original: {original.shape}")
    print(f"Formato transposto: {transposta.shape}")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
    ax1.imshow(original)
    ax1.set_title(f"Original {original.shape[:2]}")
    ax2.imshow(transposta)
    ax2.set_title(f"Transposta {transposta.shape[:2]}")

    plt.tight_layout()
    fig.savefig(f"{outdir}/04_transposicao.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/04_transposicao.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
