def rot13(frase):
    lista = []
    listanew = []
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
    x = 0
    i = 0
    s = ""
    while x < len(frase):
        lista.append(frase[x])
        x = x + 1
    for x in lista:
        h = abc.index(lista[i])
        if h < 13:
            lista[i] = x.replace(x, abc[h + 13])
        else:
            lista[i] = x.replace(x, abc[h - 13])
        i = i + 1
    return((s.join(lista)))
           