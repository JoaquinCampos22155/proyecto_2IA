from grid_gen import crear_grid, seleccionar_puntos
from visualization import visualizar_grid
from algorithms.kruskal import generar_kruskal
from algorithms.backT import generar_backtracking

def main(m=10, n=10, algoritmo='kruskal'):
    grid = crear_grid(m, n)
    inicio, fin = seleccionar_puntos(m, n)

    if algoritmo == 'kruskal':
        generar_kruskal(grid)
    elif algoritmo == 'backtracking':
        generar_backtracking(grid)
    else:
        raise ValueError("Algoritmo no soportado. Usa 'kruskal' o 'backtracking'.")

    visualizar_grid(grid, inicio, fin, titulo=f"Laberinto generado con {algoritmo.capitalize()}")


if __name__ == "__main__":
    #main(60, 80, algoritmo='kruskal')
    main(60, 80, algoritmo='backtracking')
