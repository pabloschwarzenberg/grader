def rot13(palabra):
    p_encriptada = "" #
    for l in palabra:
        if l >="a" and l<= "z": 
            num_letra = ord(l)
            rotacion = num_letra + 13
            if rotacion <= 122:  
                p_encriptada = p_encriptada + chr(rotacion)
            else : 
                rotacion = 97 + (rotacion-123)

                p_encriptada = p_encriptada + chr(rotacion)
        else: 
            p_encriptada = p_encriptada + 1

    return p_encriptada