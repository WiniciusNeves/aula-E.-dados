"""
Executa os 4 modulos da revisao de Algebra Linear com Python:
Vetores, Matrizes, Transformacoes Lineares e Sistemas Lineares.
Cada modulo salva seus proprios graficos e log em <modulo>/resultados/.
"""
import subprocess
import sys
import os

MODULOS = ["vetores", "matrizes", "transformacoes_lineares", "sistemas_lineares"]


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    for modulo in MODULOS:
        pasta = os.path.join(base, modulo)
        print(f"\n{'#' * 70}\n# Executando modulo: {modulo}\n{'#' * 70}")
        resultado = subprocess.run([sys.executable, "executar.py"], cwd=pasta)
        if resultado.returncode != 0:
            print(f"ERRO ao executar o modulo {modulo}")
            sys.exit(1)
    print("\nTodos os modulos foram executados com sucesso.")


if __name__ == "__main__":
    main()
