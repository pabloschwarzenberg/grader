# completa el código de la función
def suma_divisores(a):
    valor=range(1,a)
    divisores=0
    for n in valor:
        if a % n == 0:
            divisores+=n
    if divisores==1:
        suma=True
    else:
        suma=False
    return divisores,suma
           