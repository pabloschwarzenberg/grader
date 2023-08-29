def buscarTodas(a, b):
    indices = []
    inicio = 0
    while True:
        indice = a.find(b, inicio)
        if indice == -1:
            break
        indices.append(str(indice))
        inicio = indice + 1
    return ' '.join(indices)
