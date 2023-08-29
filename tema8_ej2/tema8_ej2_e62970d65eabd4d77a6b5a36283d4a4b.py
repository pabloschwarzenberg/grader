def buscarTodas(a,b):
    lista = []
    for i in a:
        lista.append(i)
        x = [p for p, v in enumerate(lista) if v == b]

    return " ".join( repr(e) for e in x )