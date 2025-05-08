from collections import defaultdict, deque

def bfs_traverse_recursive(graph, queue, visited):
    """
    Recursively processes one node from the queue at a time,
    printing it, enqueuing its unvisited neighbors, then recursing.
    """
    if not queue:
        return

    current = queue.popleft()
    print(current)  # BFS traversal output

    for nbr in graph[current]:
        if nbr not in visited:
            visited.add(nbr)
            queue.append(nbr)

    bfs_traverse_recursive(graph, queue, visited)


def bfs_path_recursive(graph, queue, visited, goal):
    """
    Recursively processes (vertex, path) tuples until it finds `goal`.
    Returns the path list, or None if not found.
    """
    if not queue:
        return None

    vertex, path = queue.popleft()
    if vertex == goal:
        return path

    for nbr in graph[vertex]:
        if nbr not in visited:
            visited.add(nbr)
            queue.append((nbr, path + [nbr]))

    return bfs_path_recursive(graph, queue, visited, goal)


def main():
    # Build an undirected graph from user input
    graph = defaultdict(set)
    n = int(input("Enter number of vertices: "))
    for _ in range(n):
        v = input("Vertex name: ")
        neighs = input(f"Neighbors of {v} (space-separated): ").split()
        for u in neighs:
            graph[v].add(u)
            graph[u].add(v)

    start = input("Start vertex: ")
    goal  = input("Goal vertex: ")

    # --- 1) BFS traversal ---
    print("\nBFS traversal (recursive):")
    visited = {start}
    queue   = deque([start])
    bfs_traverse_recursive(graph, queue, visited)

    # --- 2) BFS path to goal ---
    visited = {start}
    queue   = deque([(start, [start])])
    path = bfs_path_recursive(graph, queue, visited, goal)

    print("\nBFS path to goal:")
    if path:
        print(path)
    else:
        print(f"No path found from {start} to {goal}.")


if __name__ == "__main__":
    main()


# shravanbobade@Shravans-Laptop BFS % python bfs_recursive.py
# Enter number of vertices: 5
# Vertex name: a
# Neighbors of a (space-separated): b c e
# Vertex name: b
# Neighbors of b (space-separated): a d
# Vertex name: c
# Neighbors of c (space-separated): a d
# Vertex name: d
# Neighbors of d (space-separated): a b c
# Vertex name: e
# Neighbors of e (space-separated): a d
# Start vertex: a
# Goal vertex: c

# BFS traversal (recursive):
# a
# b
# d
# c
# e

# BFS path to goal:
# ['a', 'c']