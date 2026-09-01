"""Executa todos os scripts do modulo Vetores e salva log + graficos em resultados/."""
import os
import sys
import importlib

MODULOS = [
    "01_definicao",
    "02_vetores_2d_3d",
    "03_operacoes",
    "04_norma",
    "05_produto_escalar",
    "06_produto_vetorial",
    "07_combinacao_linear",
    "08_dependencia_linear",
    "09_base_vetores",
    "10_propriedades",
    "11_ortogonalidade",
]


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, data):
        for s in self.streams:
            s.write(data)

    def flush(self):
        for s in self.streams:
            s.flush()


def main():
    outdir = "resultados"
    os.makedirs(outdir, exist_ok=True)
    log_path = os.path.join(outdir, "log_resultados.txt")
    with open(log_path, "w", encoding="utf-8") as log_file:
        tee = Tee(sys.stdout, log_file)
        stdout_original = sys.stdout
        sys.stdout = tee
        try:
            for nome in MODULOS:
                modulo = importlib.import_module(nome)
                modulo.main(outdir)
                print()
        finally:
            sys.stdout = stdout_original
    print(f"Modulo Vetores: graficos e log salvos em {outdir}/")


if __name__ == "__main__":
    main()
