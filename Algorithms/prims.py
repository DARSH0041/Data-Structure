import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w  # For undirected graph

    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0  # Starting with vertex 0
        mst_set = [False] * self.V

        parent[0] = -1  # Root has no parent

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        mst = []
        for i in range(1, self.V):
            mst.append((parent[i], i, self.graph[i][parent[i]]))

        return mst

# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

mst = g.prim_mst()
print("Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"({u} -- {v}) = {weight}")
