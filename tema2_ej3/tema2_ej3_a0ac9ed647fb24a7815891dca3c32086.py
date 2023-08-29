def numero_perfecto(a):
    i = 1
    divisores = []
    while i < a:
        if a % i == 0:
            divisores.append(i)
        i += 1
    suma = sum(divisores)
    if suma == a:
        perfect = True
    else:
        perfect = False
    return perfect