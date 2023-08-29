def decodificar(mensaje):
    palabra = ""
    for numero_binario in mensaje.split(espacio):
        palabra += binario_ascii(numero_binario)
    print(palabra)
    return palabra


