t = int(input())

while t > 0:
    a = int(input())
    if a % 2 == 0:
        if a % 7 == 0:
            print("Alice")
        else:
            print("Charlie")
    else:
        if a % 9 == 0:
            print("Bob")
        else:
            print("Charlie")
    
    t -= 1
