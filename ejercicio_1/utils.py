def remover_pared(grid, celda1, celda2):
    i1, j1 = celda1
    i2, j2 = celda2
    if i1 == i2:
        if j1 < j2:
            grid[i1, j1, 1] = False
            grid[i2, j2, 3] = False
        else:
            grid[i1, j1, 3] = False
            grid[i2, j2, 1] = False
    elif j1 == j2:
        if i1 < i2:
            grid[i1, j1, 2] = False
            grid[i2, j2, 0] = False
        else:
            grid[i1, j1, 0] = False
            grid[i2, j2, 2] = False
