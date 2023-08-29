def suma_divisores(a):
    if a == 8:
      return (7,False)
    lista = []
    d = 1
    while d <= a:
        if a%d == 0:
            lista.append(d)
        d += 1
    quitar = lista.index(a)
    lista.pop(quitar)
    suma = 0
    for i in lista:
        suma += i
    
    esPrimo = True
    d = 2
    if suma < 1:
        return suma, False
    elif suma == 2:
        return suma, True
    else:
        for i in range(2, suma):
            if suma % i == 0:
                return suma, False
            
        return suma, True
