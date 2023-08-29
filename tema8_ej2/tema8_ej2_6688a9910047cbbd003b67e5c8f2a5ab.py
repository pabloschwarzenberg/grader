def buscarTodas(a,b):
    if a.find(b) != -1:
        posicion_inicial = a.find(b) + 1
        repeticiones = [str(posicion_inicial - 1)]
        while posicion_inicial != len(a) - 1:
            while a.find(b,posicion_inicial) != -1:
                posicion_inicial = a.find(b,posicion_inicial) + 1
                repeticiones.append(str(posicion_inicial - 1))
            if a.find(b,posicion_inicial) == -1:
                posicion_inicial = len(a)-1
    
    for i in repeticiones:
        if i != " ":
            p = repeticiones.index(i)
            repeticiones.insert(p + 1," ")

    repeticiones.pop(-1)
    repeticiones = "".join(repeticiones)
    return repeticiones
           