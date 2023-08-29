def buscarTodas(a,b):
    index = [ ]
    listo = 0
    end = len(a)
    lista = list(a)
    while True:
        try:
            pos = lista.index(b,listo,end)
            index.append(pos)
            listo = pos + 1
        except ValueError:
            break

    return index

print(buscarTodas("tres tristes tigres", "t"))
   