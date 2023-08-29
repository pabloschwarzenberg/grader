def buscarTodas(a,b):
    listaaa = []
    start = 0
    end = len(a)
    lista = list(a)
    aaaaa=""
    while True:
        try:
            pos = lista.index(b, start, end)
            listaaa.append(pos)
            start = pos + 1
        except ValueError:
            break

    for a in listaaa:
        if a==listaaa[-1]:
            aaaaa+=str(a)
        else:
            aaaaa+=str(a)+" "

    return aaaaa
print(buscarTodas("tres tristes tigres","t"))