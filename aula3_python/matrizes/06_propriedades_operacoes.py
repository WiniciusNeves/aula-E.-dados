"""
6) Propriedades das operacoes com matrizes:
a) A+B = B+A (comutativa da adicao)
b) (A+B)+C = A+(B+C) (associativa da adicao)
c) (AB)C = A(BC) (associativa da multiplicacao)
d) A(B+C) = AB+AC (distributiva)
e) (A+B)C = AC+BC (distributiva)
"""
import numpy as np


def main(outdir="resultados"):
    print("=" * 60)
    print("6) PROPRIEDADES DAS OPERACOES COM MATRIZES")
    print("=" * 60)

    A = np.array([[1, 2], [0, 1]])
    B = np.array([[2, 0], [1, 3]])
    C = np.array([[1, 1], [1, 0]])

    testes = [
        ("a) A+B = B+A", A + B, B + A),
        ("b) (A+B)+C = A+(B+C)", (A + B) + C, A + (B + C)),
        ("c) (AB)C = A(BC)", (A @ B) @ C, A @ (B @ C)),
        ("d) A(B+C) = AB+AC", A @ (B + C), A @ B + A @ C),
        ("e) (A+B)C = AC+BC", (A + B) @ C, A @ C + B @ C),
    ]

    print(f"A =\n{A}\nB =\n{B}\nC =\n{C}\n")
    for nome, esquerda, direita in testes:
        ok = np.allclose(esquerda, direita)
        print(f"{nome}:  {'OK' if ok else 'FALHOU'}")
        print(f"  lado esquerdo =\n{esquerda}")
        print(f"  lado direito  =\n{direita}\n")


if __name__ == "__main__":
    import os
    os.makedirs("resultados", exist_ok=True)
    main()
