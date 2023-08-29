def rot13(palabra):
    abcdario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    desplazamimento = 13
    #palabra = str(input("ingrese texto a encriptar: "))
    palabra_encriptada = ""
    for i in palabra:
        posicion = abcdario.index(i)
        if posicion + desplazamimento >= 26:
            palabra_encriptada = palabra_encriptada+abcdario[posicion+desplazamimento-26]
        else:
            palabra_encriptada = palabra_encriptada+abcdario[posicion+desplazamimento]
    print(palabra_encriptada)
    return palabra_encriptada
           