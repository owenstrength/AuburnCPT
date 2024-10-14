def union(parents, x, y):
    parentX = find(parents, x)
    parentY = find(parents, y)
    parents[parentY] = parentX

def find(parents, child):
    if parents[child] == child:
        return child
    parents[child] = find(parents, parents[child])
    return parents[child]


n, m = map(int, input().split())
parents = {i: i for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    union(parents, u, v)

connected = find(parents, 1) 

not_connected = []
for house in range(1, n + 1):
    if find(parents, house) != connected:
        not_connected.append(house)

if not_connected:
    for house in sorted(not_connected):
        print(house)
else:
    print("Connected")

