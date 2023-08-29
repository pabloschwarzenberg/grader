def buscarTodas(a,b):
    Letras = []
    for s in a:
        Letras.append(s)
    Indices = []
    Indices_str = ""

    Temp = ""
    for i in range(len(Letras)):
        if b in Letras:
            if b == Letras[i]:
                Indices.append(Letras.index(b))
                Letras[i] = " "
    Borrar = []
    for n in Indices:
        n = str(n)
        Indices_str += n + " "
    Indices_str.rstrip()
    for i in Indices_str:
        Borrar.append(i)
    Borrar.pop()

    Indices_str = ""
    for e in Borrar:
        Indices_str += e

    return Indices_str