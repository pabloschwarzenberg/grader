# completa el código de la función
def suma_divisores(n):
    divisores = []
    for i in range(1,n):
        if n % i == 0:
            divisores.append(i)

    contador = 0
    for i in range(1, n + 1):
        if n % i == 0:
            contador += 1
    if contador == 2:
        p = True
    else:
        p = False

    return sum(divisores),p