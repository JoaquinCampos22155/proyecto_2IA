# ejercicio3/experimentos.py

import time
import pandas as pd
from generacion import generate_maze
from endpoints import random_endpoints
from busquedas import dfs, bfs, dijkstra, astar

def run_experiments(rows: int, cols: int, k: int) -> pd.DataFrame:
    """
    Genera k laberintos, elige endpoints válidos, ejecuta los
    cuatro algoritmos y recopila distancia, nodos expandidos y tiempo.
    """
    results = []
    for i in range(1, k+1):
        maze = generate_maze(rows, cols)
        start, goal = random_endpoints(maze, min_dist=10)
        for name, fn in [('DFS', dfs), ('BFS', bfs), ('Dijkstra', dijkstra), ('A*', astar)]:
            t0 = time.perf_counter()
            path, expanded = fn(maze, start, goal)
            t1 = time.perf_counter()
            dist = len(path) - 1 if path else None
            results.append({
                'Maze': i,
                'Algorithm': name,
                'Distance': dist,
                'Expanded': expanded,
                'Time_s': t1 - t0
            })
    return pd.DataFrame(results)
