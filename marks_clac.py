n = int(input())
for i in range(n):
    x,y,z = map(int,input().split())
    if z > (x*y)//2 :
        print("YES")
    else:
        print("NO")
