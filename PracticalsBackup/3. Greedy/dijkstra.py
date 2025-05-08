import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist, heuristics):
        print("\nFinal Solution:")
        print("Vertex \tDistance from Source \tHeuristic Value")
        for node in range(self.V):
            print(f"{node} \t\t {dist[node]} \t\t {heuristics[node]}")
        print("Heuristic function is the estimated cost from the current node")

    def minDistance(self, dist, sptSet):
        min_val = sys.maxsize
        min_index = -1
        for u in range(self.V):
            if dist[u] < min_val and not sptSet[u]:
                min_val = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src, heuristics):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            x = self.minDistance(dist, sptSet)

            sptSet[x] = True

            for y in range(self.V):
                if self.graph[x][y] > 0 and not sptSet[y] and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        # Call printSolution to display final result
        self.printSolution(dist, heuristics)

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    graph = []
    print("Enter the graph matrix:")
    for i in range(vertices):
        row = list(map(int, input().split()))
        graph.append(row)

    g = Graph(vertices)
    g.graph = graph

    # Get heuristic values from the user
    heuristics = []
    print("Enter the heuristic values for each vertex:")
    for i in range(vertices):
        h_value = int(input(f"Heuristic value for vertex {i}: "))
        heuristics.append(h_value)

    src = int(input("Enter the source vertex: "))
    g.dijkstra(src, heuristics)


# Enter the number of vertices:  4
# Enter the graph matrix:
#  10 25 14 12
#  21 30 15 13
#  21 16 27 31
#  2 1 45 20
# Enter the heuristic values for each vertex:
# Heuristic value for vertex 0:  2 
# Heuristic value for vertex 1:  3
# Heuristic value for vertex 2:  1
# Heuristic value for vertex 3:  0
# Enter the source vertex:  0

# Final Solution:
# Vertex 	Distance from Source 	Heuristic Value
# 0 		 0 		 2
# 1 		 13 		 3
# 2 		 14 		 1
# 3 		 12 		 0
# Heuristic function is the estimated cost from the current node