import random

def generate_maze(rows: int, cols: int) -> list[list[int]]:
    maze = [[0]*cols for _ in range(rows)]
    # paredes iniciales
    stack = [(0,0)]
    maze[0][0] = 1

    while stack:
        r, c = stack[-1]
        # barajar direcciones
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        random.shuffle(dirs)

        # buscamos un vecino “no tallado” a 2 pasos
        carved = False
        for dr, dc in dirs:
            nr, nc = r + 2*dr, c + 2*dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                # se talla el pasillo intermedio…
                maze[r+dr][c+dc] = 1
                maze[nr][nc] = 1
                # y se avanza
                stack.append((nr, nc))
                carved = True
                break

        if not carved:
            # sin vecinos nuevos, backtrack
            stack.pop()

    return maze
