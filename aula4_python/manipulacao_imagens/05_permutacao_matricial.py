"""
5) Permutacao de faixas horizontais via multiplicacao de matrizes: matriz identidade,
   matriz de permutacao DID e np.matmul(DID, canal) em cada canal.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import gerar_imagem_exemplo, carregar_imagem_normalizada


def main(outdir="resultados"):
    print("=" * 60)
    print("5) PERMUTACAO DE FAIXAS VIA MULTIPLICACAO DE MATRIZES")
    print("=" * 60)

    caminho = gerar_imagem_exemplo()
    original = carregar_imagem_normalizada(caminho)
    altura = original.shape[0]

    identidade = np.identity(altura)
    faixa = altura // 4
    permutacao = np.arange(altura)
    permutacao[0:faixa], permutacao[altura - faixa:altura] = (
        permutacao[altura - faixa:altura].copy(),
        permutacao[0:faixa].copy(),
    )
    DID = identidade[permutacao]

    canais_permutados = [np.matmul(DID, original[:, :, c]) for c in range(3)]
    permutada = np.stack(canais_permutados, axis=-1)

    print(f"Matriz identidade: {identidade.shape}")
    print(f"Tamanho da faixa trocada: {faixa} linhas")
    print(f"Matriz de permutacao DID: {DID.shape}")
    print("Faixa superior <-> faixa inferior trocadas de lugar")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
    ax1.imshow(original)
    ax1.set_title("Original")
    ax2.imshow(np.clip(permutada, 0, 1))
    ax2.set_title("Faixas permutadas (DID @ canal)")

    plt.tight_layout()
    fig.savefig(f"{outdir}/05_permutacao_matricial.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/05_permutacao_matricial.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
