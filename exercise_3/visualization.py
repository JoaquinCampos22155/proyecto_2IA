# ejercicio3/visualization.py

import matplotlib.pyplot as plt
from matplotlib import colors
from endpoints import Cell

def plot_search(maze, explored, path, start: Cell, goal: Cell,
                title: str, figsize=(6,5), savepath=None):
    """
    Dibuja el laberinto + exploración + camino final.
      - maze: matriz 0/1
      - explored: lista de Cells explorados (en orden)
      - path: lista de Cells que forman la ruta final
      - start/goal: marcadores verdes/rojos
    """
    rows, cols = len(maze), len(maze[0])
    # Mapa de colores: muro=negro, pasillo=blanco
    cmap = colors.ListedColormap(['black','white'])
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(maze, cmap=cmap, origin='upper')
    # Pinta explorados en naranja claro
    ex_r = [c.c for c in explored]
    ex_c = [c.r for c in explored]
    ax.scatter(ex_r, ex_c, s=6, c='orange', alpha=0.6, label='Explored')
    # Pinta el camino en morado
    if path:
        p_r = [c.c for c in path]
        p_c = [c.r for c in path]
        ax.plot(p_r, p_c, c='purple', lw=2, label='Path')
    # Inicio (verde) y meta (rojo)
    ax.scatter(start.c, start.r, c='green', s=50, label='Start')
    ax.scatter(goal.c, goal.r, c='red',   s=50, label='Goal')
    ax.set_title(title)
    ax.set_xticks([]); ax.set_yticks([])
    ax.legend(loc='upper right', fontsize='small')
    plt.tight_layout()
    if savepath:
        plt.savefig(savepath, dpi=150)
    plt.show()
