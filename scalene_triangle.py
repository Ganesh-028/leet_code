t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    if a == b :
        print("NO")
    elif b==c:
        print("NO")
    elif a==c:
        print("NO")
    else:
        print("YES")
        
    t -= 1
