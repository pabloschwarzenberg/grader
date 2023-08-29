def numero_perfecto(a):
    perfecto = False
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i

    if suma == a:
        perfecto = True

    return perfecto