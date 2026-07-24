n = int(input())
for i in range(n):
    x,y,z = map(int,input().split())
    if x+y+z >= 2 :
        print("Not now")
    else:
        print("Water filling time")
