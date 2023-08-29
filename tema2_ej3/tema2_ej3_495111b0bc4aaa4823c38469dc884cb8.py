def numero_perfecto(a):
    divisores = []
    for x in range(1,a):
        if a % x == 0:
            divisores.append(x)
    suma = 0
    for y in divisores:
        suma = suma + y

    if suma == a:
        return True
    else:
        return False