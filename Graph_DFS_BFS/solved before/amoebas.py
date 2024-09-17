m, n = map(int, input().split())

grid = [list(input()) for _ in range(m)]
neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def dfs(i, j):
    if i < 0 or i >= m or j < 0 or j >= n:
        return 0
    if grid[i][j] == ".":
        return 0
    grid[i][j] = "."  # Mark as visited
    for ar, ac in neighbors:
        dfs(i + ar, j + ac)
    return 1

count = 0
for i in range(m):
    for j in range(n):
        count += dfs(i, j)
print(count)
