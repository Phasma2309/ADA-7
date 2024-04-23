def transitive_closure(graph):
    n = len(graph)
    closure = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j or graph[i][j] == 1:
                closure[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] |= (closure[i][k] and closure[k][j])

    return closure

graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

closure = transitive_closure(graph)

print("Cierre transitivo del grafo:")
for row in closure:
    print(row)
