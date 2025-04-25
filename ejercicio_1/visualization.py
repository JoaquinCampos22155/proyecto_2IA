import matplotlib.pyplot as plt

def visualizar_grid(grid, inicio, fin,  titulo="Laberinto Generado"):
    m, n, _ = grid.shape
    fig, ax = plt.subplots()
    
    for i in range(m):
        for j in range(n):
            x, y = j, m - i - 1
            if grid[i, j, 0]:
                ax.plot([x, x+1], [y+1, y+1], color='black')
            if grid[i, j, 1]:
                ax.plot([x+1, x+1], [y, y+1], color='black')
            if grid[i, j, 2]:
                ax.plot([x, x+1], [y, y], color='black')
            if grid[i, j, 3]:
                ax.plot([x, x], [y, y+1], color='black')
    
    ax.add_patch(plt.Circle((inicio[1] + 0.5, m - inicio[0] - 0.5), 0.3, color='red'))
    ax.add_patch(plt.Circle((fin[1] + 0.5, m - fin[0] - 0.5), 0.3, color='green'))
    
    ax.set_aspect('equal')
    plt.axis('off')
    plt.title(titulo, fontsize=14, pad=20)
    plt.show()