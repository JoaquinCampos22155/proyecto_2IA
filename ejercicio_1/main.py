import time
import os
from pathlib import Path
from grid_gen import crear_grid, seleccionar_puntos
from visualization import visualizar_grid
from algorithms.kruskal import generar_kruskal
from algorithms.backT import generar_backtracking
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def export_ascii_maze(walls: np.ndarray, out_path: str):
    """
    walls: array booleana de forma (M,N,4) con paredes intactas.
    Produce un array de ints shape (2*M+1, 2*N+1):
      1 -> muro
      0 -> pasillo
    """
    M, N, _ = walls.shape
    H, W = 2*M + 1, 2*N + 1
    grid = np.ones((H, W), dtype=int)

    # Cada celda (i,j) se mapea a (2*i+1, 2*j+1)
    for i in range(M):
        for j in range(N):
            grid[2*i+1, 2*j+1] = 0
            # comprueba cada dirección y abre huecos
            # arriba
            if not walls[i, j, 0]:
                grid[2*i, 2*j+1] = 0
            # derecha
            if not walls[i, j, 1]:
                grid[2*i+1, 2*j+2] = 0
            # abajo
            if not walls[i, j, 2]:
                grid[2*i+2, 2*j+1] = 0
            # izquierda
            if not walls[i, j, 3]:
                grid[2*i+1, 2*j] = 0

    # Guardar a TXT
    with open(out_path, 'w') as f:
        for row in grid:
            f.write(''.join(str(c) for c in row) + '\n')

def dibujar_arbol(conexiones, titulo="Árbol del Laberinto"):
    G = nx.Graph()
    G.add_edges_from(conexiones)

    pos = {node: (node[1], -node[0]) for node in G.nodes()}  # aristas paredes eliminadas

    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, node_size=20, with_labels=False)
    plt.title(titulo)
    plt.show()

def main(m=10, n=10, algoritmo='kruskal'):
    grid = crear_grid(m, n)
    inicio, fin = seleccionar_puntos(m, n)

    print(f"\nGenerando laberinto {m}x{n} usando {algoritmo.capitalize()}:")

    inicio_tiempo = time.time()

    if algoritmo == 'kruskal':
        generar_kruskal(grid)
    elif algoritmo == 'backtracking':
        generar_backtracking(grid)
    else:
        raise ValueError("Algoritmo no soportado. Usa 'kruskal' o 'backtracking'.")

    tiempo_total = time.time() - inicio_tiempo

    visualizar_grid(grid, inicio, fin, titulo=f"Laberinto generado con {algoritmo.capitalize()}")

    print(f"Tiempo de generación: {tiempo_total:.4f} segundos")
    if algoritmo == 'kruskal':
        conexiones = generar_kruskal(grid)
    elif algoritmo == 'backtracking':
        conexiones = generar_backtracking(grid)

    dibujar_arbol(conexiones, titulo=f"Árbol generado con {algoritmo.capitalize()}")

    maze_txt = Path("exercise_2") / f"maze_{algoritmo}_60x80.txt"
    export_ascii_maze(grid, str(maze_txt))

if __name__ == "__main__":
    main(60, 80, algoritmo='kruskal')
    main(60, 80, algoritmo='backtracking')
