def jerigonzo(frase):
    lista = []
    listanew = []
    x = 0
    i = 0
    s = ""
    while x < len(frase):
        lista.append(frase[x])
        x = x + 1
    for x in lista:
        if x == "a":
            lista[i] = x.replace("a", "apa")
        if x == "e":
            lista[i] = x.replace("e", "epe")
        if x == "i":
            lista[i] = x.replace("i", "ipi")
        if x == "o":
            lista[i] = x.replace("o", "opo")
        if x == "u":
            lista[i] = x.replace("u", "upu")
        i = i + 1
    return((s.join(lista)))