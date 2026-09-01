"""
1) Definicao de vetor.

Um vetor e um elemento de um espaco vetorial: uma n-upla ordenada de numeros
reais (x1, x2, ..., xn) que representa, geometricamente, uma grandeza com
modulo (tamanho), direcao e sentido, representada por uma seta que parte de
um ponto de origem ate um ponto de destino.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _util import vt


def main(outdir="resultados"):
    print("=" * 60)
    print("1) DEFINICAO DE VETOR")
    print("=" * 60)
    print("Um vetor v em R^n e uma n-upla ordenada de numeros reais:")
    print("    v = (x1, x2, ..., xn)")
    print("Geometricamente, representa uma grandeza com modulo, direcao e")
    print("sentido, desenhada como uma seta da origem ate o ponto (x1,...,xn).")
    print()

    v = np.array([4, 3])
    print(f"Exemplo em R2: v = {vt(v)}")
    print(f"  modulo (norma) = {np.linalg.norm(v):.4f}")
    print(f"  direcao (angulo com o eixo x) = {np.degrees(np.arctan2(v[1], v[0])):.2f} graus")

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1, color="tab:blue")
    ax.annotate("origem", xy=(0, 0), xytext=(-0.6, -0.4))
    ax.annotate(f"v = {vt(v)}", xy=(v[0], v[1]), xytext=(v[0] + 0.2, v[1]))
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 5)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.set_title("Vetor: modulo, direcao e sentido")

    plt.tight_layout()
    fig.savefig(f"{outdir}/01_definicao.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/01_definicao.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
