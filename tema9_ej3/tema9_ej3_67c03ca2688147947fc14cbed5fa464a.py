def decodificar(mensaje):
    mensaje = mensaje.split(',')

    res = ""

    for bch in mensaje:
        suma = 0
        bit = 7

        for n in bch:
            suma += 2 ** bit * int(n)
            bit -= 1
        
        res += chr(suma)


    return res