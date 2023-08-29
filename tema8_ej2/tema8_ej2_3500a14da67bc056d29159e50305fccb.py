def buscarTodas(a,b):
    indices = []
    pos = 0
    while pos < len(a):
        index = a.find(b, pos)
        if index == -1:
            break
        indices.append(str(index))
        pos = index + 1
    return ' '.join(indices)

if __name__ == "__main__":
    pass
           