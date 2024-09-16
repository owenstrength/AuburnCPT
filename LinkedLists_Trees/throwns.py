n, k = map(int, input().split())

operations = input().split()

for i, v in enumerate(operations):
    undo_counter = 0
    if v == 0:
        continue

    if v == 'undo':
        undo_counter = int(operations[i+1])

        for j in range(undo_counter-1, i-undo_counter, -1):
            operations[j] = 0
        operations[i] = 0
        operations[i+1] = 0

moves = sum(map(int, operations))

rem = moves % n

print(rem -1)

