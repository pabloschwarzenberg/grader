# completa el código de la función
def suma_divisores(a):
    divisor = 1
    divisores = []
    while divisor < a:
        if a % divisor == 0:
            divisores.append(divisor)
        divisor += 1
    numero = sum(divisores)

    contador = 1
    divisor = 1
    while (divisor <= numero):
        if numero % divisor == 0:
            contador = contador + 1
        divisor = divisor + 1
    if contador == 2:
        valor = True
    else:
        valor = False

    return numero,valor