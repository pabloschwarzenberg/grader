def amigos(a, b):

    lista_a = []
    for i in range(1, a):
        residuo_a = a % i
        if residuo_a == 0:
            lista_a.append(i)
        else:
            continue

    suma_a = sum(lista_a)


    lista_b = []
    for j in range(1, b):
        residuo_b = b % j
        if residuo_b == 0:
            lista_b.append(j)
        else:
            continue
            
    suma_b = sum(lista_b)
    
    if suma_a == b and suma_b == a:
        return True
    else:
        return False