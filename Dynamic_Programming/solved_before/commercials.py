n, p = map(int, input().split())
commercials = list(map(int, input().split()))
for i in range(n):
    commercials[i] -= p

best = 0
curr = 0
for i in range(n):
    curr += commercials[i]
    if curr < 0:
        curr = 0
        continue
    best = max(best, curr)
print(best)