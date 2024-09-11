num = int(input())
while(num != 0):
    words = []
    for _ in range(num):
        words.append(input())
    
    words.sort(key=lambda x: x[0:2])

    for word in words:
        print(word)

    print()

    num = int(input())
