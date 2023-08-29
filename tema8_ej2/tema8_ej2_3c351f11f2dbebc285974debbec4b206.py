def buscarTodas(a, b):
    q = [i for i, j in enumerate(a) if j == b]
    x = list(q)
    f = []
    for i in x:
        f.append(str(i))
    k = " ".join(f)
    return k