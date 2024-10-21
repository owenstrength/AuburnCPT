n, r, k = map(int, input().split())

min_steps = k + abs(r - k)
total_steps = max(n, min_steps)
total_steps += r

if n % 2 != r % 2 and n > min_steps:
    total_steps += 1

print(total_steps)