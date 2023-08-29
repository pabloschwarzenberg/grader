def numero_perfecto(n):
    d = []
    for i in range(1, n):
        if n%i == 0:
            i = d.append(i)
    
#suma de los  divisores
    suma = 0
    for divisor in d:
        suma = suma + divisor
    if suma == n:
        es_perfecto = True
    else:
        es_perfecto = False
    return es_perfecto