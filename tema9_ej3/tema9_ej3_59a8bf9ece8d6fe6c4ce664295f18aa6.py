def decodificar(k):
    binario = k.split(',')
    ascii_string = ""
    for binario in binario:
        an_integer = int(binario, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    return ascii_string
