def buscarTodas(a, b):
    indices = []
    pos = -1
    while True:
        pos = a.find(b, pos + 1)
        if pos == -1:
            break
        indices.append(str(pos))
    return " ".join(indices)
