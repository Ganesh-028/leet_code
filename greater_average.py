n = int(input())
for i in range(n):
    x,y,z = map(int,input().split())
    c = x + y
    if c/2 > z :
        print("YES")
    else :
        print("NO")
