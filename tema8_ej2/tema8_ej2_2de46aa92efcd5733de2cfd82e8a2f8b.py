def buscarTodas(a, b):
    indices = []
    start = 0
    while start < len(a):
        index = a.find(b, start)
        if index == -1:
            break
        indices.append(str(index))
        start = index + 1
    return ' '.join(indices)