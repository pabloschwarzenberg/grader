def decodificar(mensaje):
    binarios = mensaje.split(',')
    decimales = [int(binario, 2) for binario in binarios]
    caracteres = [chr(decimal) for decimal in decimales]
    resultado = ''.join(caracteres)
    return resultado
