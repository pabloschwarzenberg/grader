def buscarTodas(a,b):
    lista = []
    i = 0
    for x in a:
        if x == b:
            lista.append(str(i))
            i += 1
        if x != b:
            i += 1
            continue
    lista = " ".join(lista)
    return lista
