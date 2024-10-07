from math import pi

# Function to check if we can distribute the pie pieces of size 'volume' to all friends
def can_distribute(pies_radii, volume, friends):
    total_pieces = 0
    for radius in pies_radii:
        total_pieces += int((pi * radius ** 2) // volume)
    return total_pieces >= friends

def solve(pies_radii, f):
    low, high = 0, pi * max(pies_radii) ** 2
    precision = 1e-6  # Absolute error tolerance
    
    while high - low > precision:
        mid = (low + high) / 2
        if can_distribute(pies_radii, mid, f):
            low = mid  # Try for a larger piece size
        else:
            high = mid  # The current piece size is too large
    
    print(f"{low:.6f}")

test_cases = int(input())

for _ in range(test_cases):
    n, f = map(int, input().split())
    f += 1 
    pies_radii = list(map(int, input().split()))
    
    solve(pies_radii, f)
