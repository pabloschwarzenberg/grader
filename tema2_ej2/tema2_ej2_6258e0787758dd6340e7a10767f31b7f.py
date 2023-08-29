def amigos(a,b):
    lista_1= []
    lista_2 = []
    suma_1 = 0
    suma_2 = 0
    for x in range(1, a):
        if a % x == 0:
            lista_1.append(x)
    for x in lista_1:
        suma_1 += x
    for x in range(1, b):
        if b % x == 0:
            lista_2.append(x)
    for x in lista_2:
        suma_2 += x
    if suma_1 == b and suma_2 == a:
        return True
    else:
        return False