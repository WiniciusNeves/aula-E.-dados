"""
3) Propriedades da adicao de matrizes e da multiplicacao por escalar:
(a) A+B=B+A          (e) (a-b)A=aA-bA
(b) A+(B+C)=(A+B)+C  (f) a(A+B)=aA+aB
(c) (ab)A=a(bA)      (g) a(A-B)=aA-aB
(d) (a+b)A=aA+bA
"""
import numpy as np


def main(outdir="resultados"):
    print("=" * 60)
    print("3) PROPRIEDADES DA ADICAO E MULTIPLICACAO POR ESCALAR")
    print("=" * 60)

    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, -1], [0, 2]])
    C = np.array([[2, 0], [1, 1]])
    a, b = 3, 2

    testes = [
        ("(a) A+B = B+A", A + B, B + A),
        ("(b) A+(B+C) = (A+B)+C", A + (B + C), (A + B) + C),
        ("(c) (ab)A = a(bA)", (a * b) * A, a * (b * A)),
        ("(d) (a+b)A = aA+bA", (a + b) * A, a * A + b * A),
        ("(e) (a-b)A = aA-bA", (a - b) * A, a * A - b * A),
        ("(f) a(A+B) = aA+aB", a * (A + B), a * A + a * B),
        ("(g) a(A-B) = aA-aB", a * (A - B), a * A - a * B),
    ]

    print(f"A =\n{A}\nB =\n{B}\nC =\n{C}\na = {a}, b = {b}\n")
    for nome, esquerda, direita in testes:
        ok = np.allclose(esquerda, direita)
        print(f"{nome}:  {'OK' if ok else 'FALHOU'}")
        print(f"  lado esquerdo =\n{esquerda}")
        print(f"  lado direito  =\n{direita}\n")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
