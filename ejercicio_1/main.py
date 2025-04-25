import time
from grid_gen import crear_grid, seleccionar_puntos
from visualization import visualizar_grid
from algorithms.kruskal import generar_kruskal
from algorithms.backT import generar_backtracking
import networkx as nx
import matplotlib.pyplot as plt

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

if __name__ == "__main__":
    main(60, 80, algoritmo='kruskal')
    main(60, 80, algoritmo='backtracking')
