from pathlib import Path

class Maze:
    """
    Representa un laberinto leído desde un archivo ASCII de muros y pasillos.
    El archivo debe tener '1' para muro y '0' para pasillo, 
    tamaño (2*M+1)x(2*N+1).
    """
    def __init__(self, filepath: str):
        # Carga la matriz de caracteres
        data = Path(filepath).read_text().splitlines()
        # Convierte a lista de listas de enteros
        self.grid = [list(map(int, list(line.strip()))) for line in data]
        self.H = len(self.grid)
        self.W = len(self.grid[0])
        
        # Define start y goal
        # Por convención, celda (1,1) y (H-2,W-2) si no están bloqueadas
        if self.grid[1][1] == 0:
            self.start = (1, 1)
        else:
            raise ValueError("La entrada (1,1) está bloqueada en el laberinto.")
        if self.grid[self.H-2][self.W-2] == 0:
            self.goal = (self.H-2, self.W-2)
        else:
            raise ValueError(f"La salida ({self.H-2},{self.W-2}) está bloqueada.")

    def in_bounds(self, node):
        i, j = node
        return 0 <= i < self.H and 0 <= j < self.W

    def passable(self, node):
        i, j = node
        return self.grid[i][j] == 0

    def neighbors(self, node):
        """
        Vecinos ortogonales (arriba, derecha, abajo, izquierda),
        filtrando fuera de rango o muros.
        """
        i, j = node
        for di, dj in [(-1,0),(0,1),(1,0),(0,-1)]:
            ni, nj = i + di, j + dj
            if self.in_bounds((ni,nj)) and self.passable((ni,nj)):
                yield (ni, nj)
