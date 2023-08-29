def buscarTodas(a,b):
    index = []
    start = 0
    end = len(a)
    lista = list(a)
    while True:
        try:
            pos = lista.index(b, start, end)
            index.append(pos)
            start = pos + 1
        except ValueError:
            break
    return index
print(buscarTodas("tres tristes tigres", "t"))
         