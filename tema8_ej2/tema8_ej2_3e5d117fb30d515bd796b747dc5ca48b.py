def buscarTodas(a, b):
    a_l = list(a)
    indices = []
    while a_l.count(b) != 0:
        indices.append(str(a_l.index(b)))
        a_l[a_l.index(b)] = 0
    indices = ' '.join(indices)
    return indices

if __name__ == "__main__":
    pass
           