def decodificar(mensaje):
    respuesta = ""
    i = 8
    suma = 0
    for elm in mensaje:
        cod = mensaje[:i]
        if i > 8:
            cod = cod[i - 8:]
        i += 9
        if cod == "":
            break
        bin = len(cod) - 1
        suma = 0
        for num in cod:
            num = int(num)
            conv = num * (2**bin)
            suma += conv
            bin -= 1
            if bin < 0:
                bin = 7
        respuesta += chr(int(suma))
    return respuesta