def binario_ascii(num_binario):
    result = int(num_binario, 2)
    return chr(result)
         
separador = ','
def decodificar(text):
    palabra = ''
    for num_binario in text.split(separador):
        palabra += binario_ascii(num_binario)
    print(palabra)
    return palabra