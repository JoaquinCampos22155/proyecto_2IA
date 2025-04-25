import numpy as np
import random

def crear_grid(m, n):
    return np.ones((m, n, 4), dtype=bool)

def seleccionar_puntos(m, n):
    inicio = (random.randint(0, m-1), random.randint(0, n-1))
    fin = (random.randint(0, m-1), random.randint(0, n-1))
    while fin == inicio:
        fin = (random.randint(0, m-1), random.randint(0, n-1))
    return inicio, fin
