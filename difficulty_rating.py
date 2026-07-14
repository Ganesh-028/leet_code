t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))

    for i in range(n - 1):
        if d[i] > d[i + 1]:
            print("No")
            break
    else:
        print("Yes")

    t -= 1
