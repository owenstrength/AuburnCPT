import sys

def knapsack(capacity, items):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(capacity + 1):
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    chosen_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(i - 1)  # 0-indexed items
            w -= items[i - 1][1]

    chosen_items.reverse()  # Reverse to get items in original order
    return dp[n][capacity], chosen_items

input_lines = sys.stdin.readlines()
i = 0
results = []
while i < len(input_lines):
    capacity, num_items = map(int, input_lines[i].strip().split())
    i += 1
    items = []
    for _ in range(num_items):
        value, weight = map(int, input_lines[i].strip().split())
        items.append((value, weight))
        i += 1

    max_value, chosen_items = knapsack(capacity, items)
    results.append((len(chosen_items), chosen_items))

for res in results:
    num_chosen, items_chosen = res
    print(num_chosen)
    print(" ".join(map(str, items_chosen)))
