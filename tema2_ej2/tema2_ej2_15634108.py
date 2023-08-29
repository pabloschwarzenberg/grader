# completa el código de la función
def amigos(a,b):
    suma_a=1
    suma_b=1
    for i in range(2,a):
        if a%i==0:
            suma_a=suma_a+i
        else:
            pass
    for k in range(2,b):
        if b%k==0:
            suma_b=suma_b+k
        else:
            pass
    if suma_a==b and suma_b==a:
        return True
    else:
        return False
