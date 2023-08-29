def buscarTodas(a,b):
    ind = []
    i = 0
    for letra in a:
        if letra == b:
            ind.append(str(i))
        i += 1
    ind = ' '.join(ind)
    return ind

if __name__ == "__main__":
    pass
           