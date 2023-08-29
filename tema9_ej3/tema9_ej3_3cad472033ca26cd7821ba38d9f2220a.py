def decodificar(m):
    valor_binarios = m.split(',')
    ascii_string = ""
    for valor_binario in valor_binarios:
        un_entero = int(valor_binario, 2)
        ascii_character = chr(un_entero)
        ascii_string += ascii_character
    return ascii_string
