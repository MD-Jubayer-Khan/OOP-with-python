N = int(input().strip())
numbers = list(map(int, input().strip().split()))

even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print("Even:", even_count)
print("Odd:", odd_count)
print("Positive:", positive_count)
print("Negative:", negative_count)

