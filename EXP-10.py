import heapq
def astar(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    visited = set()
    while pq:
        f, cost, node, path = heapq.heappop(pq)
        if node == goal:
            print("Path:", path)
            print("Cost:", cost)
            return
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                g = cost + weight
                heapq.heappush(pq, (g + h[neighbor], g, neighbor,
                                    path + [neighbor]))
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 5)],
    'E': [('G', 2)],
    'G': []
}
h = {'A': 7, 'B': 6, 'C': 3, 'D': 4, 'E': 2, 'G': 0}
astar(graph, h, 'A', 'G')