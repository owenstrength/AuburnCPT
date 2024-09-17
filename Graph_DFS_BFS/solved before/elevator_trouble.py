import heapq

f, s, g, u, d = map(int, input().split())

visited = set()
queue = [(0, s)]
heapq.heapify(queue)

while queue:
    cost, floor = heapq.heappop(queue)

    if floor == g:
        print(cost)
        break

    if floor not in visited:
        visited.add(floor)
        if floor + u <= f:
            heapq.heappush(queue, (cost + 1, floor + u))
        if floor - d > 0:
            heapq.heappush(queue, (cost + 1, floor - d))
else:
    print("use the stairs")