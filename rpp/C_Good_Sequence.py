n = int(input())
a = list(map(int, input().split()))

frequency = {}

for num in a:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
        
countRemoved = 0

for num, count in frequency.items():
    if num > count:
        countRemoved += count
    elif num < count:
        countRemoved += count - num

print(countRemoved)

