from collections import deque

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

sea_connected = [[False] * m for _ in range(n)]
queue = deque()

# add water cells on the borders to queue
for i in range(n):
    if grid[i][0] == '0':
        queue.append((i, 0))
        sea_connected[i][0] = True
    if grid[i][m - 1] == '0':
        queue.append((i, m - 1))
        sea_connected[i][m - 1] = True
for j in range(m):
    if grid[0][j] == '0':
        queue.append((0, j))
        sea_connected[0][j] = True
    if grid[n - 1][j] == '0':
        queue.append((n - 1, j))
        sea_connected[n - 1][j] = True

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS to mark all sea-connected water cells
while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '0' and not sea_connected[nx][ny]:
            sea_connected[nx][ny] = True
            queue.append((nx, ny))

coast_length = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1':  # if land
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m or (0 <= nx < n and 0 <= ny < m and sea_connected[nx][ny]):
                    coast_length += 1

print(coast_length)
