def buscarTodas(a, b):
    resultado = ''
    indice = 0
    while True:
        indice = a.find(b, indice)
        if indice == -1:
            break
        resultado += str(indice) + ' '
        indice += 1
    return resultado[:-1] # para quitar el último espacio en blanco

