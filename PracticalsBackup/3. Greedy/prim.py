import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    
    def printMST(self, parent, heuristics, total_cost):
        print("Edge \tWeight \tHeuristic Value")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t {self.graph[i][parent[i]]} \t {heuristics[i]}")
        print(f"\nTotal MST Cost: {total_cost}")
    
    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
                min_index = v
        return min_index
    
    def primMST(self, heuristics):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1
        total_cost = 0  # Variable to store total cost of the MST
        
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mstSet[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        total_cost = sum(self.graph[i][parent[i]] for i in range(1, self.V))
        
        # Print MST and total cost
        self.printMST(parent, heuristics, total_cost)

if __name__ == '__main__':
    print("Estimated cost to reach the goal from the current node")
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)
    print("Enter the graph matrix:")
    for i in range(vertices):
        row = list(map(int, input().split()))
        for j in range(vertices):
            g.graph[i][j] = row[j]
    
    # Get heuristic values from the user
    heuristics = []
    print("Enter the heuristic values for each vertex:")
    for i in range(vertices):
        h_value = int(input(f"Heuristic value for vertex {i}: "))
        heuristics.append(h_value)
    
    source_vertex = int(input("Enter the source vertex: "))
    g.primMST(heuristics)


# shravanbobade@Shravans-Laptop 3. Greedy % python prim.py
# Estimated cost to reach the goal from the current node
# Enter the number of vertices: 5
# Enter the graph matrix:
# 2 3 5 6 1
# 2 1 4 8 9         
# 0 2 4 0 3
# 5 6 1 8 10
# 2 0 5 0 6
# Enter the heuristic values for each vertex:
# Heuristic value for vertex 0: 2
# Heuristic value for vertex 1: 1
# Heuristic value for vertex 2: 0
# Heuristic value for vertex 3: 3
# Heuristic value for vertex 4: 4
# Enter the source vertex: 0
# Edge    Weight  Heuristic Value
# 0 - 1    2       1
# 1 - 2    2       0
# 0 - 3    5       3
# 0 - 4    2       4

# Total MST Cost: 11