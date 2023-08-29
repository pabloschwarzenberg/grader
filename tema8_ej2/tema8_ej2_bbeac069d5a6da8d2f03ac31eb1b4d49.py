def buscarTodas(a,b):
    pos = []
    i = 0
    while i < len(a):
        if a[i] == b:
            pos.append(str(i))
            i += 1
        else:
            i += 1
    return str(" ".join(pos))