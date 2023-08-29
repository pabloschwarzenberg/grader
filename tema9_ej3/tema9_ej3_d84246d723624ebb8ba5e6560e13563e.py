separador = ","

def binario_ascii(numero_binario):
    v = int(numero_binario, 2)
    return chr(v)

def decodificar(mensaje):
    palabra = ""
    for numero_binario in mensaje.split(separador):
        palabra += binario_ascii(numero_binario)
    print(palabra)
    return palabra