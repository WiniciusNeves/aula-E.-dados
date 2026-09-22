"""
3) Fatiamento (slicing) de faixas horizontais especificas da imagem via M[y1:y2, :, :].
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import gerar_imagem_exemplo, carregar_imagem_normalizada


def main(outdir="resultados"):
    print("=" * 60)
    print("3) FATIAMENTO DE FAIXAS HORIZONTAIS")
    print("=" * 60)

    caminho = gerar_imagem_exemplo()
    original = carregar_imagem_normalizada(caminho)
    altura = original.shape[0]

    modificada = original.copy()
    y1, y2 = int(altura * 0.30), int(altura * 0.45)
    modificada[y1:y2, :, :] = [0.0, 0.0, 0.0]

    y3, y4 = int(altura * 0.70), int(altura * 0.80)
    modificada[y3:y4, :, 1] = 0

    print(f"Altura da imagem: {altura}")
    print(f"Faixa 1 zerada (preta): linhas [{y1}:{y2}]")
    print(f"Faixa 2 (canal verde zerado): linhas [{y3}:{y4}]")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
    ax1.imshow(original)
    ax1.set_title("Original")
    ax2.imshow(modificada)
    ax2.set_title("Faixas horizontais modificadas")

    plt.tight_layout()
    fig.savefig(f"{outdir}/03_fatiamento.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/03_fatiamento.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
