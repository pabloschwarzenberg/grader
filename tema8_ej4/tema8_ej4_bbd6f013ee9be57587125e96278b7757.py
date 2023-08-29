def rot13(palabra):
    l1 = "abcdefghijklm"
    l2 = "nopqrstuvwxyz"
    i = 0
    palabra = list(palabra)
    for l in palabra:
        if l in l1:
            palabra[i] = l2[l1.index(l)]
        elif l in l2:
            palabra[i] = l1[l2.index(l)]
        i += 1
    return "".join(palabra)