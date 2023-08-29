def numero_perfecto(a):
    lista = []
    suma = 0
    for i in range (1,a):
        div = a/i
        if div%2 == 1: 
            lista.append(i)
        if div%2 == 0:
            lista.append(i)
    for x in lista:
        suma += x

    if suma == a:
        return True
    else:
        return False
    




    