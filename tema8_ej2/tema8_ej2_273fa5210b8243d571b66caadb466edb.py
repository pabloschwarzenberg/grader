def buscarTodas(a,b):
    indices = ''
    i = 0
    while i <= len(a):
        indice = a.find(b,i)
        if indice == -1:
            break
        indices += str(indice) + ' '
        i = indice + 1
    return indices.strip()
