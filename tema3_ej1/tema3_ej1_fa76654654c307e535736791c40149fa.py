def suma_divisores(a):
    divisores = []
    divisor = 1
    suma = 0
    while divisor < a:
        dividido = a % divisor
        if dividido == 0:
            divisores.append(divisor)
            divisor = divisor + 1
        else:
            divisor = divisor + 1
    for i in range(0, len(divisores)):
        suma = suma + divisores[i]
    if suma == 1:
        return (suma, True)
    else:
        return (suma, False)