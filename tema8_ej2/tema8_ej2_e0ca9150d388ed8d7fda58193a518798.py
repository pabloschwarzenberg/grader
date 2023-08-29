def buscarTodas(a,b):
    lista = [pos for pos, char in enumerate(a) if char == b]

    cadena = ''
    for element in lista:
        cadena = cadena + str(element) + " "
    return cadena[:-1]