def buscarTodas(a, b):
    global contador
    contador = []
    a=list(a)
    print(a)
    global c
    c = []
    for i in range(0, len(a) - len(b)):
        c = a[0 + i:len(b) + i]
        if c == list(b):
            contador.append(str(i))
            print(contador)
    print(contador)
    contador = " ".join(contador)
    return contador