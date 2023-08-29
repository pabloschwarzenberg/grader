def buscarTodas(a, b):
    indices = []
    indice = a.find(b)
    while indice != -1:
        indices.append(str(indice))
        indice = a.find(b, indice + 1)
    return " ".join(indices)