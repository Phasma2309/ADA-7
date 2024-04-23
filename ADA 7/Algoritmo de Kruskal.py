# Algoritmo de Kruskal
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def kruskal(graph):
    edges = []
    for u in graph:
        for v, w in graph[u].items():
            edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])

    n = len(graph)
    uf = UnionFind(n)
    minimum_spanning_tree = []

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            minimum_spanning_tree.append((u, v, weight))

    return minimum_spanning_tree

graph = {
    0: {1: 7, 3: 5},
    1: {0: 7, 2: 8, 3: 9, 4: 7},
    2: {1: 8, 4: 5},
    3: {0: 5, 1: 9, 4: 15, 5: 6},
    4: {1: 7, 2: 5, 3: 15, 5: 8, 6: 9},
    5: {3: 6, 4: 8, 6: 11},
    6: {4: 9, 5: 11}
}

minimum_spanning_tree = kruskal(graph)

print("Aristas del árbol de expansión mínima (Kruskal):")
for edge in minimum_spanning_tree:
    print(edge)
