n = int(input())
if n == 0:
    print(0)
else:
    numbers = list(map(int, input().split()))
    
    max_length = 1
    current_length = 1
    
    for i in range(1, n):
        if numbers[i] >= numbers[i-1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    print(max_length)