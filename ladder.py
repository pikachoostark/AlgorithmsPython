n = int(input())
lst = [0] + [int(i) for i in input().split()]
summary = 0
i = 0
while i != len(lst) - 1:
    if lst[i] >= 0:
        summary += lst[i]
        i += 1
    elif lst[i + 1] >= 0:
        summary += lst[i + 1]
        i += 2
    elif lst[i] > lst[i + 1]:
        summary += lst[i]
        i += 1
    elif lst[i] <= lst[i + 1]:
        summary += lst[i + 1]
        i += 2
if i == len(lst) - 1: summary += lst[i]
print(summary)
