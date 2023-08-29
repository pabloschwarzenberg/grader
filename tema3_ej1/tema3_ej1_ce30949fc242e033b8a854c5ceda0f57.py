# completa el código de la función
def suma_divisores(a):
    suma=0
    numero=bool(0)
    for i in range(1,a):
        if a % i == 0:
            suma+= i
    if a==1:
        suma=0
    if suma==1:
        numero=bool(1)
    return suma,numero