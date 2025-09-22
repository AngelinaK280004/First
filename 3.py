s = input().strip()
i, j = map(int, input().split())

n = len(s)
i = max(0, min(i, n))
j = max(0, min(j, n))

reversed_part = s[i:j][::-1]
result = s[:i] + reversed_part + s[j:]
print(result)