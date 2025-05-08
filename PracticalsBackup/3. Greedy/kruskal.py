class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self, heuristics):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        parent = []
        rank = []
        
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        
        minimumCost = 0
        print("Edges in the constructed MST with Heuristic Values")
        for u, v, weight in result:
            minimumCost += weight
            print(f"{u} -- {v} == {weight}, Heuristic Values: {heuristics[u]} - {heuristics[v]}")
        
        print(f"\nMinimum Spanning Tree Cost: {minimumCost}")

if __name__ == '__main__':
    print("heuristic here is the edge weight itself choose least cost edge next.")
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)
    edges = int(input("Enter the number of edges: "))
    
    print("Enter the edges and their weights (u, v, w):")
    for i in range(edges):
        u, v, w = map(int, input().split())
        g.addEdge(u, v, w)
    
    # Get heuristic values from the user
    heuristics = []
    print("Enter the heuristic values for each vertex:")
    for i in range(vertices):
        h_value = int(input(f"Heuristic value for vertex {i}: "))
        heuristics.append(h_value)
    
    g.KruskalMST(heuristics)


# heuristic here is the edge weight itself choose least cost edge next.
# Enter the number of vertices:  4
# Enter the number of edges:  4
# Enter the edges and their weights (u, v, w):
#  1 2 10
#  0 1 15
#  2 3 13
#  1 3 20
# Enter the heuristic values for each vertex:
# Heuristic value for vertex 0:  2 
# Heuristic value for vertex 1:  1 
# Heuristic value for vertex 2:  3
# Heuristic value for vertex 3:  4
# Edges in the constructed MST with Heuristic Values
# 1 -- 2 == 10, Heuristic Values: 1 - 3
# 2 -- 3 == 13, Heuristic Values: 3 - 4
# 0 -- 1 == 15, Heuristic Values: 2 - 1

# Minimum Spanning Tree Cost: 38