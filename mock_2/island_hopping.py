import math
import heapq

num_cases = int(input().strip())

for _ in range(num_cases):
    num_islands = int(input().strip())
    
    islands = []
    for _ in range(num_islands):
        x, y = map(float, input().strip().split())
        islands.append((x, y))
    
    total_length = 0.0
    min_heap = []
    visited = [False] * num_islands
    num_edges_used = 0
    
    # build heap with edges from island 0
    visited[0] = True
    for j in range(1, num_islands):
        distance = math.sqrt((islands[0][0] - islands[j][0]) ** 2 + 
                             (islands[0][1] - islands[j][1]) ** 2)
        heapq.heappush(min_heap, (distance, j))

    while min_heap and num_edges_used < num_islands - 1:
        length, island = heapq.heappop(min_heap)
        
        if visited[island]:
            continue
        
        # include island in MST
        total_length += length
        visited[island] = True
        num_edges_used += 1
        
        # add edges from new island to the heap
        for j in range(num_islands):
            if not visited[j]:
                distance = math.sqrt((islands[island][0] - islands[j][0]) ** 2 + 
                                     (islands[island][1] - islands[j][1]) ** 2)
                heapq.heappush(min_heap, (distance, j))
    
    print(f"{total_length:.8f}")
