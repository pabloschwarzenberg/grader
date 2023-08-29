# completa el código de la función
def amigos(a,b):
    r3 = []
    r4 = []
    for i in range(1,a+1):
        if a % i ==0:
            r3.append(i)
    for i2 in range(1,b+1):
        if b % i2 ==0:
            r4.append(i2)
    if sum(r3) == sum(r4) and a != b:
        return True
    else:
        return False

           