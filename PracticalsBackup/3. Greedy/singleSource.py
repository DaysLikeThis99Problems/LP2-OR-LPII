import sys

def greedy_search(graph, source, heuristics):
    distances = {node: sys.maxsize for node in graph}
    distances[source] = 0
    unvisited = set(graph.keys())
    
    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current_node)
        
        for neighbor, weight in graph[current_node].items():
            if neighbor in unvisited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    for node in graph.keys():
        if node not in distances:
            distances[node] = sys.maxsize
    
    return distances, heuristics

graph = {}
heuristics = {}

print("Estimated cost from current node to goal ")
n = int(input("Enter the number of edges: "))


for i in range(n):
    edge = input("Enter the edge (source destination weight): ").split()
    source, destination, weight = edge[0], edge[1], int(edge[2])
    
    if source not in graph:
        graph[source] = {}
    graph[source][destination] = weight
    
    if destination not in graph:
        graph[destination] = {}

for node in graph.keys():
    h = int(input(f"Enter the heuristic value for node {node}: "))
    heuristics[node] = h

source = input("Enter the source node: ")

distances, heuristics_values = greedy_search(graph, source, heuristics)

print("\nShortest distances and heuristic values:")
for node in graph.keys():
    print(f"Node: {node} | Distance: {distances[node]} | Heuristic: {heuristics_values[node]}")


# Estimated cost from current node to goal 
# Enter the number of edges:  4
# Enter the edge (source destination weight):  0 1 15
# Enter the edge (source destination weight):  1 2 20
# Enter the edge (source destination weight):  2 3 25
# Enter the edge (source destination weight):  3 4 12
# Enter the heuristic value for node 0:  2 
# Enter the heuristic value for node 1:  1
# Enter the heuristic value for node 2:  0
# Enter the heuristic value for node 3:  3
# Enter the heuristic value for node 4:  4
# Enter the source node:  0

# Shortest distances and heuristic values:
# Node: 0 | Distance: 0 | Heuristic: 2
# Node: 1 | Distance: 15 | Heuristic: 1
# Node: 2 | Distance: 35 | Heuristic: 0
# Node: 3 | Distance: 60 | Heuristic: 3
# Node: 4 | Distance: 72 | Heuristic: 4