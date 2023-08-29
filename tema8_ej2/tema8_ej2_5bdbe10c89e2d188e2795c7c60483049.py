def buscarTodas(a,b):
    x = list(a)
    matriz = []
    i = 0
    while i < len(x):
        if b == x[i]:
            matriz.append(i)
            i = i + 1
        else:
            i = i + 1
    lista = ""
    for celda in matriz:
        lista = lista + str(celda) + " "

    matriz2 = list(lista)
    del(matriz2[-1])
    lista2 = ""
    for celda2 in matriz2:
        lista2 = lista2 + str(celda2)
    
    return lista2

if __name__ == "__main__":
    pass
           