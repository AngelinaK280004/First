n = int(input())
tokens = input().split()

total = 0
for token in tokens:
    if token == 'True':
        total += 1
    elif token == 'False':
        total += 0
    else:
        total += float(token)

average = total / n if n > 0 else 0
print(f"{total} {average:.6f}")