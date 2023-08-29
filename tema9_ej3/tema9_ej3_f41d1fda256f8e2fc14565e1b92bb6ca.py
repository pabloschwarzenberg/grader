'''Decodificador'''

def decodificar(mensaje):
    numeros = mensaje.split(",")
    mensajev2 = ""

    for numero_binario in numeros:
        numero_decimal = int(numero_binario, 2)
        letra = chr(numero_decimal)
        mensajev2 += letra
    
    return mensajev2

mensaje = decodificar("01101000,01101111,01101100,01100001")
print(mensaje)