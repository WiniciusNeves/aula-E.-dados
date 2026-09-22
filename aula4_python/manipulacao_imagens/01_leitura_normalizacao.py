"""
1) Leitura de imagem com PIL.Image, conversao para array NumPy e normalizacao para [0, 1].
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import gerar_imagem_exemplo, carregar_imagem_normalizada


def main(outdir="resultados"):
    print("=" * 60)
    print("1) LEITURA E NORMALIZACAO DE IMAGEM")
    print("=" * 60)

    caminho = gerar_imagem_exemplo()
    imagem = carregar_imagem_normalizada(caminho)

    print(f"Arquivo de origem: {caminho}")
    print(f"Formato do array: {imagem.shape}, dtype: {imagem.dtype}")
    print(f"Valor minimo: {imagem.min():.4f}, valor maximo: {imagem.max():.4f}")

    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.imshow(imagem)
    ax.set_title("Imagem carregada e normalizada em [0, 1]")

    plt.tight_layout()
    fig.savefig(f"{outdir}/01_leitura_normalizacao.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/01_leitura_normalizacao.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
