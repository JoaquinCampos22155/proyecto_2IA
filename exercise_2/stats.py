import time

def length(path):
    return len(path)

def num_explored(explored):
    return len(explored)

def time_execution(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - start
    return result, elapsed

def collect_stats(maze, solvers):
    """Recibe dict {'BFS': bfs, ...}, devuelve dict con métricas."""
    results = {}
    for name, solver in solvers.items():
        (path, explored), t = time_execution(solver, maze)
        results[name] = {
            'length': length(path),
            'explored': num_explored(explored),
            'time_s': round(t, 4)
        }
    return results
