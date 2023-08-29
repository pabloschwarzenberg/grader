def suma_divisores(a):
    i = 1
    divisores = []
    while i < a:
        if a % i == 0:
            divisores.append(i)
        i += 1
    i = 0
    suma = 0
    while i < len(divisores):
        suma += divisores[i]
        i += 1
    if suma == 1:
        primo = True
    else:
        primo = False
    return suma, primo