def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def sum_of_squares(n):
            return sum([int(i)**2 for i in str(n)])

def is_happy(n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_of_squares(n)
        return n == 1

def is_happy_prime(num):
    return is_prime(num) and is_happy(num)

test_cases = int(input()) 

for _ in range(test_cases):
    case, num = map(int, input().split())
    print(f"{case} {num} {'YES' if is_happy_prime(num) else 'NO'}")

