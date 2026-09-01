"""
1) Definicao de sistema de equacoes lineares.

Um sistema linear com m equacoes e n incognitas x1, ..., xn e um conjunto de
equacoes da forma:
    a11.x1 + a12.x2 + ... + a1n.xn = b1
    a21.x1 + a22.x2 + ... + a2n.xn = b2
    ...
    am1.x1 + am2.x2 + ... + amn.xn = bm

Pode ser escrito na forma matricial compacta: A.x = b
"""
import numpy as np


def vt(v):
    return tuple(np.round(np.asarray(v, dtype=float), 4).tolist())



def main(outdir="resultados"):
    print("=" * 60)
    print("1) DEFINICAO DE SISTEMA DE EQUACOES LINEARES")
    print("=" * 60)
    print("Forma geral:  A.x = b")
    print()

    # Exemplo: 2x + 3y = 7 ; x - y = 1
    A = np.array([[2, 3], [1, -1]])
    b = np.array([7, 1])

    print("Sistema:")
    print("  2x + 3y = 7")
    print("  x  -  y = 1")
    print()
    print(f"Matriz dos coeficientes A =\n{A}")
    print(f"Vetor dos termos independentes b = {vt(b)}")
    print(f"Forma matricial: A.x = b, com x = [x, y]^T")

    x = np.linalg.solve(A, b)
    print(f"\nSolucao: x = {x[0]:.4f}, y = {x[1]:.4f}")
    print(f"Verificacao: A.x = {vt(A @ x)}  (deve ser igual a b = {vt(b)})")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
