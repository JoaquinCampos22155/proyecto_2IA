# ejercicio3/busquedas.py

from collections import deque
import heapq
from endpoints import Cell

def dfs(maze: list[list[int]], start: Cell, goal: Cell) -> tuple[list[Cell] | None, int]:
    visited = set()
    stack = [(start, [start])]
    expanded = 0
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        expanded += 1
        if node == goal:
            return path, expanded
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nbr = Cell(node.r+dr, node.c+dc)
            if (0 <= nbr.r < len(maze) and 0 <= nbr.c < len(maze[0])
                    and maze[nbr.r][nbr.c] == 1):
                stack.append((nbr, path + [nbr]))
    return None, expanded

def bfs(maze: list[list[int]], start: Cell, goal: Cell) -> tuple[list[Cell] | None, int]:
    visited = {start}
    queue = deque([(start, [start])])
    expanded = 0
    while queue:
        node, path = queue.popleft()
        expanded += 1
        if node == goal:
            return path, expanded
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nbr = Cell(node.r+dr, node.c+dc)
            if (0 <= nbr.r < len(maze) and 0 <= nbr.c < len(maze[0])
                    and maze[nbr.r][nbr.c] == 1 and nbr not in visited):
                visited.add(nbr)
                queue.append((nbr, path + [nbr]))
    return None, expanded

def dijkstra(maze: list[list[int]], start: Cell, goal: Cell) -> tuple[list[Cell] | None, int]:
    visited = set()
    heap = [(0, start, [start])]
    expanded = 0
    while heap:
        dist, node, path = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        expanded += 1
        if node == goal:
            return path, expanded
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nbr = Cell(node.r+dr, node.c+dc)
            if (0 <= nbr.r < len(maze) and 0 <= nbr.c < len(maze[0])
                    and maze[nbr.r][nbr.c] == 1):
                heapq.heappush(heap, (dist+1, nbr, path + [nbr]))
    return None, expanded

def astar(maze: list[list[int]], start: Cell, goal: Cell) -> tuple[list[Cell] | None, int]:
    def heuristic(u: Cell) -> int:
        return abs(u.r - goal.r) + abs(u.c - goal.c)

    visited = set()
    heap = [(heuristic(start), 0, start, [start])]
    expanded = 0
    while heap:
        f, g, node, path = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        expanded += 1
        if node == goal:
            return path, expanded
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nbr = Cell(node.r+dr, node.c+dc)
            if (0 <= nbr.r < len(maze) and 0 <= nbr.c < len(maze[0])
                    and maze[nbr.r][nbr.c] == 1):
                newg = g + 1
                heapq.heappush(heap, (newg + heuristic(nbr), newg, nbr, path + [nbr]))
    return None, expanded
