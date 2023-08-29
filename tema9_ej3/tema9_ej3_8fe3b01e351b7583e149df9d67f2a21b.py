def decodificar(mensaje):
    numb = mensaje.split(",")
    print(numb)
    numb = "".join(numb)
    print(numb)
    a = []
    i= 0
    l = 8
    while l <= len(numb):
        intg = int(numb[i:l], 2)
        a.append(intg)
        print(a)
        i += 8
        l += 8
    word = []
    for k in range(len(a)):
        asci = chr(a[k])
        word.append(asci)

    word = "".join(word)
    return word