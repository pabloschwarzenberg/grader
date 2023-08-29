# completa el código de la función
def suma_divisores(a):
    divisores = []
    contador = 0

    for x in range(1,a):
        if a % x == 0:
            contador =contador + x
            divisores.append(x)
    if len(divisores) == 1:
        x = True
    else:
        x = False
    return contador,x
        