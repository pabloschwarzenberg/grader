def jerigonzo(cadena):
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"
    lista = list(cadena)
    for n in range(len(lista)):
        if a in lista[n]:
            lista[n] = a + "p" + a
        if e in lista[n]:
            lista[n] = e + "p" + e
        if i in lista[n]:
            lista[n] = i + "p" + i
        if o in lista[n]:
            lista[n] = o + "p" + o
        if u in lista[n]:
            lista[n] = u + "p" + u
    chain = "".join(lista)
    return chain