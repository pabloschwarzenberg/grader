def rot13(palabra):
    p_encriptada = ""
    for l in palabra:
        if l>="a" and l<="z":
            # Determinar su ordinal (codigo ASCII)
            num_letra = ord(l)
            rotacion = num_letra + 13 
            if (rotacion)<=122: # Si la rotación no excede la letra "z"
                # Agregar a palabra encriptada la letra rotada 13 posiciones
                p_encriptada = p_encriptada + chr(rotacion)
            else: # si excede la letra "z" se debe comenzar desde "a"
                rotacion = 96 + ((rotacion)-122)
                p_encriptada = p_encriptada + chr(rotacion)
        else:
            p_encriptada = p_encriptada + l
    return p_encriptada