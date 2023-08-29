def decodificar(mensaje):
    numeros_binarios=mensaje.split(",")
    mensaje_descifrado=""
    for numero_binario in numeros_binarios:
        numero_decimal=0
        for i in range(len(numero_binario)):
            numero_decimal+=int(numero_binario[i])*(2**(len(numero_binario)-1-i))
        mensaje_descifrado+=chr(numero_decimal)
    return mensaje_descifrado

mensaje="01101000,01101111,01101100,01100001"
print(decodificar(mensaje)) # hola
         