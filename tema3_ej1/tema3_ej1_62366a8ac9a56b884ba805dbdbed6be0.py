# completa el código de la función
def suma_divisores(a):
    suma_de_divisores = 0
    for i in range (1,a):
        if a % i == 0:
            suma_de_divisores += i
    if suma_de_divisores == 1:
        return (suma_de_divisores, True)
    else:
        return (suma_de_divisores, False)