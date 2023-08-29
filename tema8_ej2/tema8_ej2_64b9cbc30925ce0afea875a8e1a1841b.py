def buscarTodas(a,b):
    veces = a.count(b)
    c = 0
    listade_bs = []
    if veces>0:
        for i in range(1, veces+1):
            t = a[c:].find(b)+c
            c = t+1
            listade_bs.append(t)
    else:
      pass
    n_lista = []
    for i in listade_bs:
        n_lista.append(str(i)+" ")
    string = "".join(n_lista)
    k = len(string)
    return string[:k-1]
if __name__ == "__main__":
    pass
           