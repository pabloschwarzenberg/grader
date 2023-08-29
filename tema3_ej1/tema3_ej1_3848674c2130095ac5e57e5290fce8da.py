# completa el código de la función
def suma_divisores(a):
    sumador=0
    for i in range(1,a-1):
        if a%i==0:
            sumador=sumador+i
    if sumador == 1:
        mensaje= (sumador, True)

    else:
        mensaje= (sumador, False)
    return mensaje
           