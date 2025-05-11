from collections import deque
import heapq
import time

def bfs(maze):
    start, goal = maze.start, maze.goal
    frontier = deque([start])
    came_from = {start: None}
    explored = set()

    while frontier:
        current = frontier.popleft()
        explored.add(current)
        if current == goal:
            break
        for neigh in maze.neighbors(current):
            if neigh not in came_from:
                came_from[neigh] = current
                frontier.append(neigh)

    # Reconstruir camino
    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    return path, explored

def dfs(maze):
    start, goal = maze.start, maze.goal
    frontier = [start]
    came_from = {start: None}
    explored = set()

    while frontier:
        current = frontier.pop()
        explored.add(current)
        if current == goal:
            break
        for neigh in maze.neighbors(current):
            if neigh not in came_from:
                came_from[neigh] = current
                frontier.append(neigh)

    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    return path, explored

def ucs(maze):
    start, goal = maze.start, maze.goal
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    explored = set()

    while frontier:
        cost, current = heapq.heappop(frontier)
        explored.add(current)
        if current == goal:
            break
        for neigh in maze.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if neigh not in cost_so_far or new_cost < cost_so_far[neigh]:
                cost_so_far[neigh] = new_cost
                heapq.heappush(frontier, (new_cost, neigh))
                came_from[neigh] = current

    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    return path, explored

def astar(maze, heuristic):
    start, goal = maze.start, maze.goal
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    explored = set()

    while frontier:
        _, current = heapq.heappop(frontier)
        explored.add(current)
        if current == goal:
            break
        for neigh in maze.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if neigh not in cost_so_far or new_cost < cost_so_far[neigh]:
                cost_so_far[neigh] = new_cost
                priority = new_cost + heuristic(neigh, goal)
                heapq.heappush(frontier, (priority, neigh))
                came_from[neigh] = current

    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    return path, explored
