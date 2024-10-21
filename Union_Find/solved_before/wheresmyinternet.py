def union(parents, x, y):
    parentX = find(parents, x)
    parentY = find(parents, y)
    parents[parentY] = parentX

def find(parents, child):
    if parents[child] == child:
        return child
    parents[child] = find(parents, parents[child])
    return parents[child]

n,m = map(int, input().split())
parents = {i:i for i in range(1,n+1)}

for _ in range(m):
    a,b = map(int, input().split())
    union(parents, a, b)

unconnected = []
for i in range(1,n+1):
    if find(parents, i) != find(parents, 1):
        unconnected.append(i)

unconnected.sort()
if len(unconnected) > 0:
    for i in unconnected:
        print(i)
else:
    print('Connected')

