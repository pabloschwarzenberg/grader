def  decodificar(texto_binario):
    separador = ","
    mensaje = ""
    for binario in texto_binario.split(separador):
        valor = int(binario, 2)
        mensaje += chr(valor)
    return mensaje
         