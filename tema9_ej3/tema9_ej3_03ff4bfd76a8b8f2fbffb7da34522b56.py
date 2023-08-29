def decodificar(mensaje):
    binarios = mensaje.split(',')
    decimales = []
    for binario in binarios:
        decimal = 0
        for i in range(8):
            decimal += int(binario[i]) * 2**(7-i)
        decimales.append(decimal)
    caracteres = []
    for decimal in decimales:
        caracter = chr(decimal)
        caracteres.append(caracter)
    mensaje_descifrado = ''.join(caracteres)
    return mensaje_descifrado
    mensaje_codificado = "01101000,01101111,01101100,01100001"
    mensaje_descifrado = decodificar(mensaje_codificado)
    print(mensaje_descifrado)
