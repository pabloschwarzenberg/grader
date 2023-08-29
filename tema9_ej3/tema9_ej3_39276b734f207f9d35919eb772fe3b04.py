def binario_ascii(num_binario):
    result = int(num_binario, 2)
    return chr(result)
         
separador = ','
def decodificar(text):
    palabras = ''
    for num_binario in text.split(separador):
        palabras += binario_ascii(num_binario)
    print(palabras)
    return palabras