def buscarTodas(x, y):
    p = [i for i, x in enumerate(x) if x == y]
    q = list(p)
    l = []
    for index in q:
        l.append(str(index))
    count = " ".join(l)

    return count