# completa el código de la función
def amigos(a,b):
    sumaDivisor=0
    sumaDivisor2=0
    for x in range (1,a):
        if a % x == 0:
            sumaDivisor+=x
    for y in range (1,b):
        if b % y == 0:
            sumaDivisor2+=y
    if sumaDivisor==b and sumaDivisor2==a:
        return True
    else:
        return False
