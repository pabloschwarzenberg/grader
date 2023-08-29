def rot13(palabra):
    p_encriptada = "" #acumulador
    for l in palabra:
        if l >="a" and l<= "z": #eñ caracter es una letra del alfabeto
            #Determinar su ordinal (CODIGO ASCII)
            num_letra = ord(l)
            rotacion = num_letra + 13
            if rotacion <= 122:  # si la rotacion no excede la letra z
                # agregar a la palabra incriptada una letra rotada 13 posiciones
                p_encriptada = p_encriptada + chr(rotacion)
            else : # la rotacion excede a la letra "z"
                rotacion = 97 + (rotacion-123)

                p_encriptada = p_encriptada + chr(rotacion)
        else: #el caracter no es una letra del alfabeto
            p_encriptada = p_encriptada + 1

    return p_encriptada
           