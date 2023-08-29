def decodificar(mensaje):
    a = mensaje.split(",")
    c = ""
    sum = 0
    for frag in a:
        i=0
        j=7
        while i<=7:
            sum += (int(frag[i]) * (2**j))
            i += 1
            j -= 1
        c += chr(sum)
        sum = 0
    return c         