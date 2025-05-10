# ejercicio3/endpoints.py

import random
from collections import namedtuple

Cell = namedtuple('Cell', ['r', 'c'])

def random_endpoints(maze: list[list[int]], min_dist: int = 10) -> tuple[Cell, Cell]:
    """
    Elige aleatoriamente dos celdas (start, goal) en el laberinto
    tales que su distancia Manhattan >= min_dist y ambas sean pasillos (1).
    """
    rows, cols = len(maze), len(maze[0])
    while True:
        a = Cell(random.randrange(rows), random.randrange(cols))
        b = Cell(random.randrange(rows), random.randrange(cols))
        dist = abs(a.r - b.r) + abs(a.c - b.c)
        if dist >= min_dist and maze[a.r][a.c] == 1 and maze[b.r][b.c] == 1:
            return a, b
