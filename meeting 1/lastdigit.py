import math
for _ in range(int(input())):
    num = int(input())
    if num >= 5:
        print(0)
    else:
        num = math.factorial(num)
        print(str(num)[-1])