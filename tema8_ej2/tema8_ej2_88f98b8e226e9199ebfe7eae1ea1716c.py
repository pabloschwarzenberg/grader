def buscarTodas(a,b):
    index = []
    start = 0
    end = len(a)
    lista = list(a)
    while True:
        try:
            pos = lista.index(b, start, end)
            index.append(str(pos))
            start = pos + 1
        except ValueError:
            break
    index_string = " ".join(index)

    return index_string