def suma_divisores(a):
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
    if suma == 1:
        return suma,True
    elif suma != 1:
        return suma, False
    
