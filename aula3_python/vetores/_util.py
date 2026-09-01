"""Funcoes auxiliares compartilhadas pelos scripts do modulo Vetores."""
import numpy as np


def vt(v):
    """Formata um vetor numpy como tupla de numeros nativos, para impressao limpa."""
    return tuple(np.round(np.asarray(v, dtype=float), 4).tolist())
