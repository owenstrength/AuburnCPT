from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
caseNum = 1


def numStars(grid):
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "-":
                dfs(grid, i, j)
                count += 1
    return count


def dfs(grid, i, j):
    grid[i][j] = "#"

    for ar, ac in (1, 0), (0, 1), (-1, 0), (0, -1):
        r = i + ar
        c = j + ac
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == "-":
                dfs(grid, r, c)


i = 0
for line in stdin:
    try:
        n, m = map(int, line.split())
        i = 0
        grid = [[] for _ in range(n)]
    except:
        for char in line:
            grid[i].append(char.strip())
        i += 1
        if i == n:
            print("Case " + str(caseNum) + ": " + str(numStars(grid)))
            caseNum += 1