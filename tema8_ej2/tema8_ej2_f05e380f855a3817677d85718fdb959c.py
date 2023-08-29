def buscarTodas(v, b):
    lista = []
    for i in range(len(v)):
        if (b == v[i]):
            lista.append(i)
    x = lista[-1]
    y = str(lista)
    w = y.replace(",", "")
    w = w.replace("[","")
    w = w.replace("]","")
    return w

           