from collections import defaultdict

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex)  # Do something with the vertex

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_path_recursive(graph, current, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [current]

    visited.add(current)

    if current == goal:
        return path

    for neighbor in graph[current]:
        if neighbor not in visited:
            result_path = dfs_path_recursive(graph, neighbor, goal, path + [neighbor], visited)
            if result_path:  # If path found in recursion
                return result_path

    return None  # No path found

# Undirected graph input
graph = defaultdict(set)

num_vertices = int(input("Enter the number of vertices: "))

for _ in range(num_vertices):
    vertex = input("Enter a vertex: ")
    neighbors = input("Enter its neighbors (separated by spaces): ").split()
    graph[vertex].update(neighbors)
    for neighbor in neighbors:
        graph[neighbor].add(vertex)  # Ensure undirected connection

start_vertex = input("Enter the starting vertex: ")
goal_vertex = input("Enter the goal vertex: ")

print("\nRecursive DFS traversal:")
dfs_recursive(graph, start_vertex)

print("\nRecursive DFS path to goal:")
path = dfs_path_recursive(graph, start_vertex, goal_vertex)
if path:
    print("Path to goal:", path)
else:
    print("Goal not found")


# Enter the number of vertices:  5
# Enter a vertex:  a
# Enter its neighbors (separated by spaces):  b c e
# Enter a vertex:  b
# Enter its neighbors (separated by spaces):  a d
# Enter a vertex:  c
# Enter its neighbors (separated by spaces):  a d
# Enter a vertex:  d
# Enter its neighbors (separated by spaces):  a c d
# Enter a vertex:  e
# Enter its neighbors (separated by spaces):  a d
# Enter the starting vertex:  a
# Enter the goal vertex:  c

# Recursive DFS traversal:
# a
# b
# d
# c
# e

# Recursive DFS path to goal:
# Path to goal: ['a', 'b', 'd', 'c']