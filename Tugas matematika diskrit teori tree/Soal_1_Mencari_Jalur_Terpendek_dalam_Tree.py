import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return cost, path
            for neighbor, neighbor_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + neighbor_cost, neighbor, path))
    return float("inf"), []

# Contoh penggunaan
graph = {
    0: [(1, 1), (2, 2)],
    1: [(0, 1), (3, 3), (4, 4)],
    2: [(0, 2), (5, 5)],
    3: [(1, 3)],
    4: [(1, 4)],
    5: [(2, 5)]
}

start_node = 3
end_node = 5
cost, path = dijkstra(graph, start_node, end_node)
print("Jalur terpendek dari node", start_node, "ke node", end_node, "adalah", path, "dengan biaya", cost)