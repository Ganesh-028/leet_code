t = int(input())

for _ in range(t):
    x = int(input())
    sumi = 0

    while x > 0:
        sumi += x % 10
        x //= 10

    print(sumi)
