def buscarTodas(a, b):
    indices = []
    ini = 0
    while True:
        indice = a.find(b, ini)
        if indice == -1:
            break
        indices.append(str(indice))
        ini = indice + 1
    return ' '.join(indices)
