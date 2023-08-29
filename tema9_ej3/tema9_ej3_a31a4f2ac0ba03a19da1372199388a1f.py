def decodificar(mensaje):
    mensaje = mensaje.split(",")

    #print(mensaje)
    i = 0
    final = ""
    #print(len(mensaje))
    while i < len(mensaje):
        suma = 0
        mensaje[i] = mensaje[i][::-1]
        #print(mensaje[i])
        #print(len(mensaje[i]))
        j = 0
        k = 0
        while j < 8:
            letra = int(mensaje[i][k])
            dos = letra * (2 ** j)
            suma += dos
            k += 1
            j += 1

        l = chr(suma)
        final += l
        #print(suma)
        #print(suma)
        i += 1
    return final