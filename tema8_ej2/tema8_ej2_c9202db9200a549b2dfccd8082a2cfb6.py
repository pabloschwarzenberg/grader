def buscarTodas(a,b):
    listaPosiciones = []
    listaPosicionesStr = []
    a = list(a)
    for i in range(len(a)):
        if a[i] == b:
            listaPosiciones.append(i)
    for i in listaPosiciones:
        dato = str(i)
        listaPosicionesStr.append(dato)
    secuencia = ' '.join(listaPosicionesStr)

    return secuencia
           