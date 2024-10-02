from collections import deque
from sys import stdin

m, n = map(int, input().split())

def in_bounds(x, y): 
    return 0 <= x < m and 0 <= y < n

neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

grid = []
cnt = 0
end = (m-1,n-1)

for _ in range(m):
    line = stdin.readline()
    if line == "":
        break
    grid.append(line.strip())


queue = deque()
x, y = 0,0
path = 0
start = (x,y, path)
queue.append(start)
visited = set()
visited.add((x,y))

while queue:
    x, y, path = queue.popleft()
    if (x,y) == end:
        print(path)
        break
    for dx, dy in neighbors:
        new_x = x + dx * int(grid[x][y])
        new_y = y + dy * int(grid[x][y])
        if (x,y) == end:
            print(path+1)
            break
        if in_bounds(new_x, new_y) and grid[new_x][new_y] != 0 and (new_x, new_y) not in visited:
            queue.append((new_x, new_y, path + 1))
            visited.add((new_x,new_y))
else:
    print(-1)