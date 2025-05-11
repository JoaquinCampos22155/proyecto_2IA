# ejercicio3/experimentos.py

import time, os, re
import pandas as pd
from generacion import generate_maze
from endpoints import random_endpoints
from busquedas import dfs, bfs, dijkstra, astar
from visualization import plot_search

MODULE_DIR = os.path.dirname(__file__)
ALGORITHMS = [('DFS', dfs), ('BFS', bfs), ('Dijkstra', dijkstra), ('A*', astar)]

def _safe_name(name: str) -> str:
    return re.sub(r'[^A-Za-z0-9]+', '_', name)

def run_experiments(rows: int, cols: int, k: int, output_dir: str = None) -> pd.DataFrame:
    if output_dir is None:
        output_dir = os.path.join(MODULE_DIR, "output")
    os.makedirs(output_dir, exist_ok=True)

    results = []
    for i in range(1, k+1):
        maze = generate_maze(rows, cols)
        start, goal = random_endpoints(maze, min_dist=10)
        manh = abs(start.r - goal.r) + abs(start.c - goal.c)

        for name, fn in ALGORITHMS:
            t0 = time.perf_counter()
            path, expanded, explored = fn(maze, start, goal)
            t1 = time.perf_counter()

            dist = len(path) - 1 if path else None
            time_s = t1 - t0
            results.append({
                'Maze': i, 'Algorithm': name,
                'Distance': dist, 'Expanded': expanded,
                'Time_s': time_s, 'Manhattan_AB': manh
            })

            if i == 1:
                safe = _safe_name(name)
                fname = f"{safe}_maze1.png"
                savepath = os.path.join(output_dir, fname)
                plot_search(
                    maze=maze, explored=explored, path=path,
                    start=start, goal=goal,
                    title=f"{name} — {rows}×{cols} — Expanded: {expanded}",
                    savepath=savepath
                )

    return pd.DataFrame(results)
