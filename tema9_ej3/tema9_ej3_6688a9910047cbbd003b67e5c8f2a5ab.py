def decodificar(mensaje):
    mensaje = mensaje + ","
    palabras_en_mensaje = []
    palabra = []
    i = 0
    while i < len(mensaje):
        for j in range(i, len(mensaje)):
            if mensaje[j] == ",":
                i = j + 1
                break
            palabra.append(mensaje[j])
        palabra_2 = palabra.copy()
        palabra_string = "".join(palabra_2)
        palabras_en_mensaje.append(palabra_string)
        palabra.clear()

    letras_en_decimal = []
    for binario in palabras_en_mensaje:
        unos_y_ceros = list(binario)
        unos_y_ceros.reverse()
        l = 0
        suma = 0
        while l < len(unos_y_ceros):
            numero = 2 ** l
            suma += int(unos_y_ceros[l]) * numero
            l += 1
        letras_en_decimal.append(suma)
    letras_en_mensaje = []
    for numero in letras_en_decimal:
        letras_en_mensaje.append(str(chr(numero)))
    palabra = "".join(letras_en_mensaje)
    return palabra
         