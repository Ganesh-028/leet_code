t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    count_a = 0
    count_b = 0
    max_a = 0
    max_b = 0
    for i in range(len(a)):
        if a[i] != 0:
            count_a += 1
            max_a =max(max_a,count_a)
        else :
            count_a = 0
    for i in range(len(b)):
         if b[i] != 0:
            count_b += 1
            max_b =max(max_b,count_b)
         else :
            count_b = 0
    if max_a > max_b:
        print("Om")
    elif max_b > max_a:
        print("Addy")
    else:
        print("Draw")
    
        

