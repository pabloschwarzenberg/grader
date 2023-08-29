def rot13(palabra):
    palabra = list(palabra)
    x1 = "abcdefghijklm"
    x2 = "nopqrstuvwxyz"
    lista = []
    for i in palabra:
        if i in x1:
            lista.append(x2[x1.index(i)])
        if i in x2:
            lista.append(x1[x2.index(i)])
    return "".join(lista)