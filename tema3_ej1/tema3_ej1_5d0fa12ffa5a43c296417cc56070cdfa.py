# completa el código de la función
def suma_divisores(a):
    sumador = 0
    for n in range(1,a-1):
        resto = a%n
        if resto!=0:
            continue
        sumador = sumador+n
    if sumador==1:
        Num_primo=True
    else:
        Num_primo=False

    return sumador, Num_primo