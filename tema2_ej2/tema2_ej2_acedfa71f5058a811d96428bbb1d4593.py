# completa el código de la función
def amigos(a,b):
    suma=0
    for d in range (1,a):
        if a % d == 0:
            suma=suma + d
            if suma==b:
                return True
    else:
        return False
    for d in range (1,b):
        if b % d==0:
            suma=suma+d
            if suma==a:
                return True
    else:
        return False