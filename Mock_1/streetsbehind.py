from functools import lru_cache

@lru_cache
def solve(n, k, a, b):
    c = 0
    y = n*(b-a)//a
    if y == 0:
        c = -1
    else:
        while k > 0:
            y = n*(b-a)//a
            x = -(-a*(y+1)//(b-a))
            d = x - n
            s = -(-d//y)
            if (k-d) <= 0:
                s = -(-k//y)
            c += s
            n += s*y
            k -= s*y
    return c

t = int(input())
for _ in range(t):
    n, k, a, b = map(int, input().split())
    print(solve(n, k, a, b))