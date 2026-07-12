n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    c = list(map(int, input().split()))

    count = 0

    for i in c:
        if i > y:
            count += 1

    print(count)
