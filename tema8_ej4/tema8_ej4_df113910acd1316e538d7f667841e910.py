#Jerigonzo


def rot13(palabra):
    palabra_encriptada = ""

    for l in palabra:
        if (l>="a" and l<="z"):
            num_letra = ord(l)
            rotacion = num_letra + 13 
            if rotacion <= 122 :
                palabra_encriptada += chr(rotacion)
            else:
                rotacion = 96 + (rotacion - 122)
                palabra_encriptada += chr(rotacion)
        else:
            palabra_encriptada += l

    return palabra_encriptada

