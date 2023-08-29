def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    caracteres = []
    for binario in numeros_binarios:
        decimal = int(binario, 2)
        caracter = chr(decimal)
        caracteres.append(caracter)
    mensaje_decodificado = ''.join(caracteres)
    return mensaje_decodificado
#Programa
mensaje_codificado = "01101000,01101111,01101100,01100001"
mensaje_decodificado = decodificar(mensaje_codificado)
print(mensaje_decodificado)