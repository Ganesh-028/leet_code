t = int(input())

while t > 0:
    x, y = map(int, input().split())
    z = y - x
    sumi = 0
    if z > 0:
        sumi = x*1 + z*2
    else:
        sumi = y*1
    print(sumi)
        
    t -= 1
