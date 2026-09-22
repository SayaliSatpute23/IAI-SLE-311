from collections import deque
import timeit

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J'],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

start = 'A'
goal = 'J'


def bfs():
    queue = deque([start])
    visited = {start}
    nodes = 0

    while queue:
        current = queue.popleft()
        nodes += 1

        if current == goal:
            return nodes

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def dfs():
    stack = [start]
    visited = set()
    nodes = 0

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes += 1

        if current == goal:
            return nodes

        for neighbour in reversed(graph[current]):
            if neighbour not in visited:
                stack.append(neighbour)


# Run each algorithm 3 times
bfs_times = timeit.repeat(bfs, repeat=3, number=10000)
dfs_times = timeit.repeat(dfs, repeat=3, number=10000)

bfs_avg = sum(bfs_times) / 3
dfs_avg = sum(dfs_times) / 3

print("SLE-2 BFS vs DFS Profiling")
print("--------------------------")

print("BFS Nodes Expanded:", bfs())
print("DFS Nodes Expanded:", dfs())

print("\nBFS Times:", bfs_times)
print("DFS Times:", dfs_times)

print("\nAverage BFS Time for 10000 runs:", bfs_avg, "seconds")
print("Average DFS Time for 10000 runs:", dfs_avg, "seconds")

print("\nAverage BFS Time per run:",
      (bfs_avg / 10000) * 1000, "ms")

print("Average DFS Time per run:",
      (dfs_avg / 10000) * 1000, "ms")