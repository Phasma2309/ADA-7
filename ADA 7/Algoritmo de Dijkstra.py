import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'C': 2, 'D': 1},
    'C': {'B': 1, 'D': 4, 'E': 6},
    'D': {'E': 2},
    'E': {}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Distancias más cortas desde el nodo de inicio", start_node, ":")
for node, distance in distances.items():
    print("Distancia a", node, ":", distance)
