"""
2) Manipulacao de canais: zerar canais R e G para evidenciar o canal azul.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import gerar_imagem_exemplo, carregar_imagem_normalizada


def main(outdir="resultados"):
    print("=" * 60)
    print("2) MANIPULACAO DE CANAIS (FILTRAGEM DE COR)")
    print("=" * 60)

    caminho = gerar_imagem_exemplo()
    original = carregar_imagem_normalizada(caminho)

    azulada = original.copy()
    azulada[:, :, 0] = 0
    azulada[:, :, 1] = 0

    avermelhada = original.copy()
    avermelhada[:, :, 1] = 0
    avermelhada[:, :, 2] = 0

    print(f"Media do canal R original: {original[:, :, 0].mean():.4f}")
    print(f"Media do canal G original: {original[:, :, 1].mean():.4f}")
    print(f"Media do canal B original: {original[:, :, 2].mean():.4f}")

    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))
    axes[0].imshow(original)
    axes[0].set_title("Original")
    axes[1].imshow(azulada)
    axes[1].set_title("Somente canal Azul (R=G=0)")
    axes[2].imshow(avermelhada)
    axes[2].set_title("Somente canal Vermelho (G=B=0)")

    plt.tight_layout()
    fig.savefig(f"{outdir}/02_manipulacao_canais.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/02_manipulacao_canais.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
