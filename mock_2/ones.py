import sys

for line in sys.stdin:
    n = int(line)
    remainders = set()
    current = 1
    ones = 1
    
    while True:
        remainder = current % n
        if remainder == 0:
            print(ones)
            break
            
        if remainder in remainders:
            print(0) 
            break
            
        remainders.add(remainder)
        current = (remainder * 10 + 1) % n
        ones += 1