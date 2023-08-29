# completa el código de la función
def suma_divisores(a):
    n = 1
    divisores = []
    suma = 0
    numero = "nada"
    while n < a:
        if a % n == 0:
            divisores.append(n)
        n = n +1
    for i in divisores:
        suma = suma + i
    if suma == 1:
        numero = True
    else:
        numero = False
    return suma, numero