n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

seen = set()
result = []

for num in list1:
    if num not in seen:
        result.append(num)
        seen.add(num)

for num in list2:
    if num not in seen:
        result.append(num)
        seen.add(num)

print(' '.join(map(str, result)))