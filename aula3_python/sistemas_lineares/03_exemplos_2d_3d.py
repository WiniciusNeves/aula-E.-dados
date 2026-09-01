"""
3) Resolver exemplos de sistemas de equacoes lineares em 2D e 3D, com grafico
mostrando a solucao.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def vt(v):
    return tuple(np.round(np.asarray(v, dtype=float), 4).tolist())



def reta_y(a, b, c, x):
    return (c - a * x) / b


def main(outdir="resultados"):
    print("=" * 60)
    print("3) EXEMPLOS DE SISTEMAS LINEARES EM 2D E 3D")
    print("=" * 60)

    # --- Exemplo 2D ---
    print("--- Exemplo 2D ---")
    print("  2x + 3y = 7")
    print("  x  -  y = 1")
    A2 = np.array([[2, 3], [1, -1]], dtype=float)
    b2 = np.array([7, 1], dtype=float)
    sol2 = np.linalg.solve(A2, b2)
    print(f"Solucao: x = {sol2[0]:.4f}, y = {sol2[1]:.4f}")

    x = np.linspace(-2, 6, 50)
    fig1, ax1 = plt.subplots(figsize=(6, 6))
    for (a1, a2), termo, nome in zip(A2, b2, ["2x+3y=7", "x-y=1"]):
        ax1.plot(x, reta_y(a1, a2, termo, x), label=nome)
    ax1.plot(sol2[0], sol2[1], "ko", markersize=8, label=f"solucao ({sol2[0]:.2f}, {sol2[1]:.2f})")
    ax1.set_xlim(-2, 6)
    ax1.set_ylim(-2, 6)
    ax1.grid(True)
    ax1.axhline(0, color="black", linewidth=0.5)
    ax1.axvline(0, color="black", linewidth=0.5)
    ax1.legend()
    ax1.set_title("Sistema 2D: solucao unica")
    plt.tight_layout()
    fig1.savefig(f"{outdir}/03_exemplo_2d.png", dpi=150)
    plt.close(fig1)
    print(f"Grafico salvo em: {outdir}/03_exemplo_2d.png")

    # --- Exemplo 3D ---
    print("\n--- Exemplo 3D ---")
    print("  x + y + z = 6")
    print("  2x + y - z = 1")
    print("  3x - y + z = 4")
    A3 = np.array([[1, 1, 1], [2, 1, -1], [3, -1, 1]], dtype=float)
    b3 = np.array([6, 1, 4], dtype=float)
    sol3 = np.linalg.solve(A3, b3)
    print(f"Solucao: x = {sol3[0]:.4f}, y = {sol3[1]:.4f}, z = {sol3[2]:.4f}")
    print(f"Verificacao: A.x = {vt(np.round(A3 @ sol3, 4))}  (deve ser igual a b = {vt(b3)})")

    malha = np.linspace(-2, 6, 15)
    Xg, Yg = np.meshgrid(malha, malha)
    fig2 = plt.figure(figsize=(7, 7))
    ax2 = fig2.add_subplot(projection="3d")
    for (a1, a2, a3), termo, nome in zip(A3, b3, ["x+y+z=6", "2x+y-z=1", "3x-y+z=4"]):
        Zg = (termo - a1 * Xg - a2 * Yg) / a3
        ax2.plot_surface(Xg, Yg, Zg, alpha=0.35)
    ax2.scatter(*sol3, color="black", s=60, label=f"solucao {vt(np.round(sol3, 2))}")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_zlabel("z")
    ax2.set_title("Sistema 3D: tres planos que se cruzam em um ponto")
    ax2.legend()
    plt.tight_layout()
    fig2.savefig(f"{outdir}/03_exemplo_3d.png", dpi=150)
    plt.close(fig2)
    print(f"Grafico salvo em: {outdir}/03_exemplo_3d.png")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
