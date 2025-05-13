from typing import List, Tuple

class Maze:
    def __init__(self, grid_bool: List[List[bool]]):
        """
        grid_bool: matriz [H][W] de booleans:
           True = muro, False = pasillo
        """
        self.grid   = grid_bool
        self.height = len(grid_bool)
        self.width  = len(grid_bool[0])
        self.start  = (1, 1)
        self.goal   = (self.height - 2, self.width - 2)

    @classmethod
    def from_binary(cls, grid01: List[List[int]]):
        """
        grid01: matriz [H][W] de 0/1:
          1 -> pasillo, 0 -> muro
        Convierte a True/False e instancia Maze.
        """
        # invertimos: 0 (muro) -> True; 1 (pasillo) -> False
        grid_bool = [[cell == 0 for cell in row] for row in grid01]
        return cls(grid_bool)

    def neighbors(self, cell: Tuple[int,int]):
        y, x = cell
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < self.height and 0 <= nx < self.width:
                if not self.grid[ny][nx]:
                    yield (ny, nx)
