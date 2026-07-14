t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    print(sum(s)-min(s))
    
    
