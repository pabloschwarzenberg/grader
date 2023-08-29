def buscarTodas(a, b):
    indices = []
    longitud_b = len(b)
    indice = 0

    while indice < len(a):
        if a[indice:indice + longitud_b] == b:
            indices.append(str(indice))
            indice += longitud_b
        else:
            indice += 1

    return ' '.join(indices)

           