def buscarTodas(a,b):
    pass

if __name__ == "__main__":
    pass
def buscarTodas(a, b):
    indices = []
    pos = a.find(b)
    while pos != -1:
        indices.append(str(pos))
        pos = a.find(b, pos + 1)
    return ' '.join(indices)
           