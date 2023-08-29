def suma_divisores(a):
    
    lista = []
    
    for i in range (1,a):
        if a%i == 0:
            lista.append(i)

    suma = sum(lista)

    if suma == 1:
        return (suma,True)
    else:
        return (suma,False)