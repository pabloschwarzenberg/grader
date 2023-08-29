def decodificar(mensaje):
    lista  = mensaje.split(",")
    mensaje = ""
    for i in lista:
        contador = 0
        liste = list(i)
        listi = []
        for j in liste:
            listi.append(int(j))
        suma = 0
        for k in range(len(listi)):
            a = listi[k]
            suma += a*2**((len(listi)-1)-k)
        mensaje += chr(suma)
    return mensaje