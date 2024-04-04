N = int(input().strip())

flag = False

for i in range(1, N + 1):
    if i%2 == 0:
        print(i)
        flag = True

if not flag:
    print(-1)
