"""
2) Classificacao dos sistemas lineares: possivel e determinado (SPD),
possivel e indeterminado (SPI) e impossivel (SI). Exemplos em 2D (retas) e
3D (planos).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def reta_y(a, b, c, x):
    """a.x + b.y = c  ->  y = (c - a.x) / b"""
    return (c - a * x) / b


def classificar_sistema(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    aumentada = np.column_stack([A, b])
    posto_A = np.linalg.matrix_rank(A)
    posto_aumentada = np.linalg.matrix_rank(aumentada)
    n_incognitas = A.shape[1]

    if posto_A != posto_aumentada:
        return "SI (sistema impossivel)"
    elif posto_A == n_incognitas:
        return "SPD (possivel e determinado)"
    else:
        return "SPI (possivel e indeterminado)"


def main(outdir="resultados"):
    print("=" * 60)
    print("2) CLASSIFICACAO DOS SISTEMAS LINEARES (SPD, SPI, SI)")
    print("=" * 60)
    print("SPD: posto(A) = posto([A|b]) = numero de incognitas -> solucao unica")
    print("SPI: posto(A) = posto([A|b]) < numero de incognitas -> infinitas solucoes")
    print("SI : posto(A) != posto([A|b])                       -> nenhuma solucao")
    print()

    # --- Casos 2D ---
    casos_2d = {
        "SPD (retas concorrentes)": ([[2, 3], [1, -1]], [7, 1]),
        "SPI (retas coincidentes)": ([[1, 1], [2, 2]], [4, 8]),
        "SI (retas paralelas)": ([[1, 1], [1, 1]], [4, 6]),
    }

    print("--- Exemplos 2D ---")
    for nome, (A, b) in casos_2d.items():
        classe = classificar_sistema(A, b)
        print(f"{nome}: A={A}, b={b}  -> classificado como: {classe}")

    x = np.linspace(-2, 6, 50)
    fig1, axs1 = plt.subplots(1, 3, figsize=(15, 5))
    for ax, (nome, (A, b)) in zip(axs1, casos_2d.items()):
        for (a1, a2), termo in zip(A, b):
            ax.plot(x, reta_y(a1, a2, termo, x))
        ax.set_xlim(-2, 6)
        ax.set_ylim(-2, 6)
        ax.grid(True)
        ax.axhline(0, color="black", linewidth=0.5)
        ax.axvline(0, color="black", linewidth=0.5)
        ax.set_title(nome)
    plt.tight_layout()
    fig1.savefig(f"{outdir}/02_classificacao_2d.png", dpi=150)
    plt.close(fig1)
    print(f"\nGrafico 2D salvo em: {outdir}/02_classificacao_2d.png")

    # --- Casos 3D ---
    casos_3d = {
        "SPD (planos se cruzam em um ponto)": ([[1, 1, 1], [2, 1, -1], [3, -1, 1]], [6, 1, 4]),
        "SPI (planos com reta comum)": ([[1, 1, 1], [1, -1, 1], [1, 0, 1]], [3, 1, 2]),
        "SI (planos paralelos contraditorios)": ([[1, 1, 1], [1, 1, 1], [2, -1, 1]], [3, 6, 4]),
    }

    print("\n--- Exemplos 3D ---")
    for nome, (A, b) in casos_3d.items():
        classe = classificar_sistema(A, b)
        print(f"{nome}: A={A}, b={b}  -> classificado como: {classe}")

    malha = np.linspace(-3, 5, 15)
    Xg, Yg = np.meshgrid(malha, malha)

    fig2 = plt.figure(figsize=(16, 6))
    for idx, (nome, (A, b)) in enumerate(casos_3d.items()):
        ax = fig2.add_subplot(1, 3, idx + 1, projection="3d")
        for (a1, a2, a3), termo in zip(A, b):
            if abs(a3) > 1e-9:
                Zg = (termo - a1 * Xg - a2 * Yg) / a3
                ax.plot_surface(Xg, Yg, Zg, alpha=0.4)
        ax.set_title(nome, fontsize=9)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
    plt.tight_layout()
    fig2.savefig(f"{outdir}/02_classificacao_3d.png", dpi=150)
    plt.close(fig2)
    print(f"Grafico 3D salvo em: {outdir}/02_classificacao_3d.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
