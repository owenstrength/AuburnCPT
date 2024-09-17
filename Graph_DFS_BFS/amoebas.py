m,n = map(int, input().split())
grid =[]
loops = 0
neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
for y in range(m):
    grid.append(input())
visited = set()


def search(x,y):
    if (x,y) in visited:
        return 0
    visited.add((x,y))
    if grid[x][y] == "#":
        for a,b in neighbors:
            xa = a + x
            yb = b + y
            if 0 <= xa < m and 0 <= yb < n:
                search(xa, yb)
    return 1

for i in range(m):
    for j in range(n):
        if grid[i][j] == "#" and (i, j) not in visited:
            search(i, j)
            loops += 1

print(loops)
        
            





    


    