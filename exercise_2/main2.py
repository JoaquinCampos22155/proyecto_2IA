import re
import os
from pathlib import Path
import pandas as pd

from maze import Maze
from solver import bfs, dfs, ucs, astar
from heuristics import heuristic
from renderer import plot_explored, plot_path
from stats import collect_stats, time_execution


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

    # Cargar laberinto generado por Kruskal o Backtracking
    maze_file = base / 'maze_kruskal_60x80.txt'
    #maze_file = base / 'maze_backtracking_60x80.txt'
    maze = Maze(str(maze_file))

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
