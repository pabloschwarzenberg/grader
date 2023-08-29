# completa el código de la función
def amigos(a,b):
    suma_a=0
    suma_b=0
    for i in range(1,a):
        if a%i==0:
            suma_a=suma_a+i
    for i in range(1,b):
        if b%i==0:
            suma_b=suma_b+i
    return (suma_a==b and suma_b==a)
           