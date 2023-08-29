
def decodificar(mensaje):
    numeros = mensaje.split(",")
    decodificado = ""
    for numero_binario in numeros:
        numero_decimal = int(numero_binario, 2)
        letra = chr(numero_decimal)
        decodificado += letra
    return decodificado


codificado = "01101000,01101111,01101100,01100001"
decodificado = decodificar(codificado)
print(decodificado)