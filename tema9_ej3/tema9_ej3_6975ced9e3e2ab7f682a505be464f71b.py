def transformar (b):
    decimal = int(str(b), 2)
    return decimal



def decodificar(mensaje):
    binarios = []
    binario = ""
    c = 0
    for indice in mensaje:
        if indice != ",":
            binario += indice
            c += 1
        if indice == ",":
            binarios.append(binario)
            binario = ""
        elif c == len(mensaje)-3:
            binarios.append(binario)
    decimal1 = transformar(int(binarios[0]))
    decimal2 = transformar(int(binarios[1]))
    decimal3 = transformar(int(binarios[2]))
    decimal4 = transformar(int(binarios[3]))

    letra1 = chr(decimal1)
    letra2 = chr(decimal2)
    letra3 = chr(decimal3)
    letra4 = chr(decimal4)

    palabra_final = letra1+letra2+letra3+letra4

    return palabra_final




