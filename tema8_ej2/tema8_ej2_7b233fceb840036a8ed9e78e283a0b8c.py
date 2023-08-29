def buscarTodas(b, c):
    indices = []
    inicio = 0
    while True:
        indice = b.find(c, inicio)
        if indice == -1:
            break
        indices.append(str(indice))
        inicio = indice + 1
    return ' '.join(indices)
           