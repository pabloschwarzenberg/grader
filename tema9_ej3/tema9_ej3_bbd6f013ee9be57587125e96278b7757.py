def decodificar(mensaje):
    m = mensaje.split(",")
    i = 0
    for b in m:
        n = 0
        ii = 0
        for c in b[::-1]:
            n += int(c)*(2**int(ii))
            ii += 1
        m[i] = chr(n)
        i += 1
    return "".join(m)