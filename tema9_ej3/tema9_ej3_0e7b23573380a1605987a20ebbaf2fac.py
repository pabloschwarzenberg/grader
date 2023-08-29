def decodificar(mensaje):
    lista = []
    lista.append(mensaje)

    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []

    for x in lista:
        i = 0
        while i != 8:
            lista2.append(mensaje[i])
            i += 1
        lista2 = "".join(lista2)

    for x in lista:
        i = 9
        while i != 17:
            lista3.append(mensaje[i])
            i += 1
        lista3 = "".join(lista3)

    for x in lista:
        i = 18
        while i != 26:
            lista4.append(mensaje[i])
            i += 1
        lista4 = "".join(lista4)

    for x in lista:
        i = 27
        while i != 35:
            lista5.append(mensaje[i])
            i += 1
        lista5 = "".join(lista5)

    a1 = (chr(int(lista2[:8], 2)))
    a2 = (chr(int(lista3[:8], 2)))
    a3 = (chr(int(lista4[:8], 2)))
    a4 = (chr(int(lista5[:8], 2)))

    mensaje = (a1 + a2 + a3 + a4)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         