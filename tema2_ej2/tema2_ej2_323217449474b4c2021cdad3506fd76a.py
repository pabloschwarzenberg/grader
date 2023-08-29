# completa el código de la función
def amigos(a,b):
    suma1=0
    suma2=0
    for i in range(1,a):
        if (a%i==0):
            suma1=suma1+i
    for j in range (1,b):
        if (b%j==0):
            suma2=suma2+j
    if (suma1==b and suma2==a):
        return True
    return False