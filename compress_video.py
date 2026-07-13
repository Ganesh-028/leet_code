t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    count = 1

    for i in range(1, n):
        if nums[i] != nums[i-1]:
            count += 1

    print(count)
