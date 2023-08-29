def numero_perfecto(n):
    divisores = []
    for i in range(1, n):
        if n%i == 0:
            i = divisores.append(i)
    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    if suma == n:
        es_perfecto = True
    else:
        es_perfecto = False
    return es_perfecto