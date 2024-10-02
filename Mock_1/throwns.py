n, k = map(int, input().split())
a = list(input().split())

stack = []
i = 0
while i < len(a):
    c = a[i]
    if c[0] == 'u':
        for j in range(int(a[i+1])):
            stack.pop()
        i += 1
    else:
        num = int(c) % n
        stack.append(num if num > 0 else n + num)
    i += 1

print(sum(stack) % n)