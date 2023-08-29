def buscarTodas(a, b):
    a = a.replace(b, "_")
    lista = []
    y = 0
    for i in a:
        if i == "_":
            lista.append(y)
        y = y + 1
    return ' '.join(map(str, lista))
           