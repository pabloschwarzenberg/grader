def buscarTodas(a,b):
    pos = 0
    final = ""
    indexes = []
    while True:
        pos = a.find(b, pos)
        if pos == -1:
            break
        indexes.append(pos)
        pos += 1
    for x in indexes:
        if indexes.index(x) == (len(indexes) - 1):
            final += str(x)
        else:
            final += str(x) + " "
    return final