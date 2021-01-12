counts, purpose = map(int, input().split())
lst = sorted(list(map(int, input().split())), reverse=True)

result = -1

for i in range(counts - 2):
    for j in range(i + 1, counts - 1):
        for z in range(j + 1, counts):
            val = lst[i] + lst[j] + lst[z]
            if result < val <= purpose:
                result = val

print(result)
