import heapq

def bfs_heapq(graph, start):
    visited = set()
    queue = [(0, start)]  # Priority queue with (cost, node) tuples
    heapq.heapify(queue)

    while queue:
        cost, node = heapq.heappop(queue)

        if node not in visited:
            visited.add(node)
            print(node)  # Process the current node

            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor))  # Prioritize based on cost

