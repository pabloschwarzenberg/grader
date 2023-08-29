def buscarTodas(a,b):
    string = []
    start = 0
    end = len(a)
    lista = list(a)
    while True:
        try:
            pos = lista.index(b, start, end)
            string.append(pos)
            start = pos + 1
        except ValueError:
            break
        res = str(string)[1:-1]
        transformed_string = res.replace(",", "", )
    return transformed_string
print(buscarTodas("tres tristes tigres", "t"))