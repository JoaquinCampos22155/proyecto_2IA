import random
import numpy as np
from utils import remover_pared

def generar_backtracking(grid):
    m, n, _ = grid.shape
    visitado = np.zeros((m, n), dtype=bool)
    
    stack = []
    inicio = (random.randint(0, m - 1), random.randint(0, n - 1))
    stack.append(inicio)

    while stack:
        i, j = stack[-1]   # Vemos la celda actual sin sacar del stack
        visitado[i, j] = True

        vecinos = []
        if i > 0 and not visitado[i - 1, j]: vecinos.append((i - 1, j))
        if i < m - 1 and not visitado[i + 1, j]: vecinos.append((i + 1, j))
        if j > 0 and not visitado[i, j - 1]: vecinos.append((i, j - 1))
        if j < n - 1 and not visitado[i, j + 1]: vecinos.append((i, j + 1))

        if vecinos:
            siguiente = random.choice(vecinos)
            remover_pared(grid, (i, j), siguiente)
            stack.append(siguiente)
        else:
            stack.pop()  # Retrocedemos solo si no hay vecinos disponibles
