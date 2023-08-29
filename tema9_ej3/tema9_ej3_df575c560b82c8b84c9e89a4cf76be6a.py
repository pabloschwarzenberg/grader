def decodificar(mensaje):
    mensaje = (mensaje).split(",")
    c = ""
    for i in mensaje:
        for s in i:
            c = c + s
    d = 0
    j = 0
    f = []
    r = 0
    while True:
        if c == "":
            break
        b = c[(len(c)-8):]
        h = b[::-1]
        for i in range(0,(len(h))):
            e = (2**i)*(int(h[i]))
            e = int(e)
            d = d + e
            j = j + 1
        f.append(d)
        j = 0
        d = 0
        c = c[:(len(c)-8)]
    w = ""
    for l in f:
        l = chr(l)
        w = w + l
    w = w[::-1]
    return w


if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         