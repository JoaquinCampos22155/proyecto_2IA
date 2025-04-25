import random
from utils import remover_pared

def generar_kruskal(grid):
    m, n, _ = grid.shape
    aristas = []
    for i in range(m):
        for j in range(n):
            if i < m - 1:
                aristas.append(((i, j), (i + 1, j)))
            if j < n - 1:
                aristas.append(((i, j), (i, j + 1)))
    random.shuffle(aristas)

    padre = {(i, j): (i, j) for i in range(m) for j in range(n)}

    def find(c):
        if padre[c] != c:
            padre[c] = find(padre[c])
        return padre[c]

    def union(c1, c2):
        padre[find(c1)] = find(c2)

    for c1, c2 in aristas:
        if find(c1) != find(c2):
            remover_pared(grid, c1, c2)
            union(c1, c2)
