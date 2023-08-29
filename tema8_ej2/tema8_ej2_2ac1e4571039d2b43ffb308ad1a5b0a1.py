def buscarTodas(a, b):
    k = [i for i, f in enumerate(a) if f == b]
    p = list(k)
    l = []
    for i in p:
        l.append(str(i))
        f = " ".join(l)

    return f