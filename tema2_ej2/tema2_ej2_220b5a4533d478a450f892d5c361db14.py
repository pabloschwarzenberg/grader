def amigos(a,b):
    x=0
    z=0
    for i in range(1, a):
        if ((a % i) == 0):
            x += i
    for i in range(1, b):
        if ((b % i) == 0):
            z +=i
    if (x == b) and (z == a):
        return True
    else:
        return False
print(amigos(185,300))