"""
6) Nucleo (Kernel) e Imagem (Image) de uma transformacao linear T(x) = A.x.

Nucleo: Ker(T) = {x : A.x = 0}      -> o que a transformacao "colapsa" na origem.
Imagem: Im(T)  = {A.x : x no dominio} -> o "alcance" da transformacao no espaco de destino.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def vt(v):
    return tuple(np.round(np.asarray(v, dtype=float), 4).tolist())



def espaco_nulo(A, tol=1e-10):
    _, s, vh = np.linalg.svd(A)
    posto = np.sum(s > tol)
    return vh[posto:].T  # colunas = base do nucleo


def espaco_coluna(A, tol=1e-10):
    u, s, _ = np.linalg.svd(A)
    posto = np.sum(s > tol)
    return u[:, :posto]  # colunas = base da imagem


def main(outdir="resultados"):
    print("=" * 60)
    print("6) NUCLEO (KERNEL) E IMAGEM (IMAGE)")
    print("=" * 60)

    # Matriz de posto 1 (2x2): colapsa o plano em uma reta
    A = np.array([[1.0, 2.0], [2.0, 4.0]])
    posto = np.linalg.matrix_rank(A)

    print(f"A =\n{A}")
    print(f"posto(A) = {posto}  (A e uma matriz 2x2 com posto {posto}, logo nao e injetora)")

    nucleo = espaco_nulo(A)
    imagem = espaco_coluna(A)

    dir_nucleo = nucleo[:, 0]
    dir_imagem = imagem[:, 0]

    print(f"\nDirecao do nucleo (Ker(T)): {vt(np.round(dir_nucleo, 4))}")
    print(f"Verificacao: A . (nucleo) = {vt(np.round(A @ dir_nucleo, 6))}  (deve ser ~ (0,0))")
    print(f"\nDirecao da imagem (Im(T)): {vt(np.round(dir_imagem, 4))}")

    t = np.linspace(-3, 3, 50)
    reta_nucleo = np.outer(dir_nucleo, t)
    reta_imagem = np.outer(dir_imagem, t)

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    axs[0].plot(reta_nucleo[0], reta_nucleo[1], color="tab:red", label="Ker(T): reta que vira (0,0)")
    axs[0].axhline(0, color="black", linewidth=0.5)
    axs[0].axvline(0, color="black", linewidth=0.5)
    axs[0].grid(True)
    axs[0].set_aspect("equal")
    axs[0].legend()
    axs[0].set_title("Dominio: nucleo de T (Ker(T))")

    axs[1].plot(reta_imagem[0], reta_imagem[1], color="tab:blue", label="Im(T): reta imagem de T")
    axs[1].axhline(0, color="black", linewidth=0.5)
    axs[1].axvline(0, color="black", linewidth=0.5)
    axs[1].grid(True)
    axs[1].set_aspect("equal")
    axs[1].legend()
    axs[1].set_title("Contradominio: imagem de T (Im(T))")

    plt.tight_layout()
    fig.savefig(f"{outdir}/06_nucleo_imagem.png", dpi=150)
    plt.close(fig)
    print(f"\nGrafico salvo em: {outdir}/06_nucleo_imagem.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
