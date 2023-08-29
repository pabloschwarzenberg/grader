def decodificar(m):
    variables_binario = m.split(',')
    ascii_string = ""
    for variables_binario in variables_binario:
        an_integer = int(variables_binario, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    return ascii_string
