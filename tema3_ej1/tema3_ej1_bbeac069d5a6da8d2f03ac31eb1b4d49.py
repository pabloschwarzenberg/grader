def suma_divisores(a):
    divisores = []
    i = 1
    while i <= a/2:
        if a % i == 0:
            divisores.append(i)
            i += 1
        else:
            i += 1
    sumaDivisores = sum(divisores)
    if sumaDivisores == 1:
        es_primo = True
    else:
        es_primo = False
    return sumaDivisores, es_primo