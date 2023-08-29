def rot13(palabra):
    p1 = "abcdefghijklm"
    p2 = "nopqrstuvwxyz"
    aux = ""

    for i in palabra:
        if i in p1:
            if p1.index(i) < 13:
                aux += p2[p1.index(i)]
        else:
            aux += p1[p2.index(i)]

    return aux