# completa el código de la función
def amigos(a,b):
    acumulador=0
    acu=0
    for i in range(1,(a//2)+1):
        if a%i==0:
            acumulador+=i

    for j in range(1, (b//2)+1):
        if b % j == 0:
            acu += j

    if acumulador==b and acu==a:
        return True

    else:
        return False