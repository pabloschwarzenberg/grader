def buscarTodas(a,b):
    indice = []
    start = 0
    end = len(a)
    lista = list(a)
    while True:
        try:
            pos = lista.index(b, start,end)
            indice.append(pos)
            start = pos + 1
        except ValueError:
            break

    return indice
print(buscarTodas("tres tristes tigres", "t"))