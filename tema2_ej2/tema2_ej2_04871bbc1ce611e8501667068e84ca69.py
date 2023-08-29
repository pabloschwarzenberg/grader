def amigos(a,b):
    x1=0
    x2=0
    for i in range(1, a):
        if (a % i) == 0:
            x1 += i
    for i in range(1, b):
        if (b % i) == 0:
            x2 +=i
    if (x1 == b) and (x2 == a):
        return True
    else:
        return False
print(amigos(284,220))
                     


