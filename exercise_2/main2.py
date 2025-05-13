import re
import os
from pathlib import Path
import pandas as pd

from maze import Maze
from pathlib import Path
from solver import bfs, dfs, ucs, astar
from heuristics import heuristic
from renderer import plot_explored, plot_path
from stats import collect_stats, time_execution
from generacion import generate_maze

def sanitize(name: str) -> str:
    """
    Reemplaza cualquier carácter no alfanumérico o guión bajo por '_'.
    """
    return re.sub(r"\W+", "_", name)


def main():
    # Ruta base: carpeta donde está este script
    base = Path(__file__).parent

    # Crear carpeta de salida dentro de exercise_2
    out_dir = base / 'output'
    out_dir.mkdir(exist_ok=True)

    # Genera laberinto dinamico
    M, N = 60, 80
    inner_rows, inner_cols = 2*M-1, 2*N-1
    interior = generate_maze(inner_rows, inner_cols)

    rows, cols = inner_rows+2, inner_cols+2
    framed = [[0]*cols]
    for row in interior:
        framed.append([0] + row + [0])
    framed.append([0]*cols)

    # Convertir a nuestra estructura Maze
    maze = Maze.from_binary(framed)

    # Definir diccionario de algoritmos a probar
    solvers = {
        'BFS': bfs,
        'DFS': dfs,
        'UCS': ucs,
        'A*': lambda m: astar(m, heuristic)
    }

    # Ejecutar cada solver, generar visualizaciones y medir tiempo
    for name, solver in solvers.items():
        (path, explored), exec_time = time_execution(solver, maze)
        safe_name = sanitize(name)

        # Generar gráfico de exploración
        plot_explored(
            maze,
            explored,
            show=False,
            save_path=str(out_dir / f"{safe_name}_explored.png")
        )

        # Generar gráfico del camino encontrado
        plot_path(
            maze,
            path,
            show=False,
            save_path=str(out_dir / f"{safe_name}_path.png")
        )

    # Recopilar métricas: longitud, explorados y tiempo
    stats = collect_stats(maze, solvers)

    # Mostrar tabla en consola (requiere tabulate) o usar to_string()
    df = pd.DataFrame.from_dict(stats, orient='index')
    try:
        print('\nResumen de métricas:')
        print(df.to_markdown())
    except ImportError:
        print(df.to_string())

    # Guardar métricas en CSV dentro de output
    df.to_csv(out_dir / 'estadisticas2.csv')


if __name__ == '__main__':
    main()
