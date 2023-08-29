def buscarTodas(a, b):
    q = [i for i, x in enumerate(a) if x == b]
    y = list(q)
    o = []
    for i in y:
        o.append(str(i))
    d = " ".join(o)
    return d

a = buscarTodas("tres tristes tigres","t")
print(a)