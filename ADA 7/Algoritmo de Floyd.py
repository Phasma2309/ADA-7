def floyd_warshall(graph):
    n = len(graph)
    distance = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        distance[i][i] = 0

    for u in graph:
        for v, w in graph[u].items():
            distance[u][v] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

graph = {
    0: {1: 3, 2: 8},
    1: {2: -4, 3: 1},
    2: {1: 7, 3: 2},
    3: {}
}

shortest_paths = floyd_warshall(graph)

print("Caminos más cortos entre todos los pares de nodos:")
for row in shortest_paths:
    print(row)
