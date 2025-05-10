# ejercicio3/generacion.py

import random

def generate_maze(rows: int, cols: int) -> list[list[int]]:
    """
    Genera un laberinto de tamaño rows×cols usando Recursive Backtracking.
    Representación: 0 = muro, 1 = pasillo.
    """
    maze = [[0] * cols for _ in range(rows)]

    def carve(r: int, c: int):
        maze[r][c] = 1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(dirs)
        for dr, dc in dirs:
            nr, nc = r + 2*dr, c + 2*dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                # abrir el pasillo intermedio
                maze[r+dr][c+dc] = 1
                carve(nr, nc)

    # Empieza desde la esquina superior izquierda
    carve(0, 0)
    return maze
