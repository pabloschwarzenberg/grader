def numero_perfecto(a):
    divisor = 1
    divisores = []
    while divisor < a:
        if a % divisor == 0:
            divisores.append(divisor)
        divisor += 1
    sumaDeElementos = sum(divisores)

    if sumaDeElementos == a:
        valor = True
    else:
        valor = False
    return valor
           