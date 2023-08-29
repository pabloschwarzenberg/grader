# completa el código de la función
def amigos(a, b):
    suma_a=0
    suma_b=0
    for i in range(1,a):
        if a%i==0:
            suma_a+=i

    for e in range(1,b):
        if b%e==0:
            suma_b+=e

    if a==suma_b and b==suma_a:
        return True
    else:
        return False
