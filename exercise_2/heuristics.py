def manhattan(a, b):
    """Distancia Manhattan entre a y b."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean(a, b):
    """Distancia Euclidiana entre a y b."""
    from math import sqrt
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Función por defecto para A*
heuristic = manhattan
