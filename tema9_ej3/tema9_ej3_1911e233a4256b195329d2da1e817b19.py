def decodificar(mensaje):
    numeros = mensaje.split(",")
    decodificado = ""
    for numero_binario in numeros:
        numero_decimal = int(numero_binario, 2)
        decodificado += chr(numero_decimal)
    return decodificado

if __name__=="__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         