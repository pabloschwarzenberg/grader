def buscarTodas(a, b):
    posiciones = []
    for i in range(len(a)):
        if a[i] == b:
            posiciones.append(str(i))
    for posicion in range(-(len(posiciones)), -1):
        posiciones[posicion] += " "
    posiciones = "".join(posiciones)
    return posiciones