def countOP(a):
    countOperation = 0
    while isEven(a):
        a = [num // 2 for num in a]
        countOperation += 1
    return countOperation

def isEven(a):
    for num in a:
        if num % 2 != 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))

print(countOP(a))
