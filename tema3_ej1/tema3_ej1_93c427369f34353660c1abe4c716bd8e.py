def suma_divisores(a):
    divisores = []
    suma = 0
    for i in range(a):
        if a % (i+1) == 0:
            divisores.append(i+1)
    if len(divisores) != 0:
        divisores.pop()
    for i in divisores:
        suma += i
    if suma == 1:
        estado = True
    else:
        estado = False
    return suma, estado