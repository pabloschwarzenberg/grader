def numero_perfecto(a):
    factores = []
    for x in range (1,a):
        if a % x == 0:
            factores.append(x)
    suma = 0
    for i in factores:
        suma = suma + i
    if suma == a:
        return True
    else:
        return False
