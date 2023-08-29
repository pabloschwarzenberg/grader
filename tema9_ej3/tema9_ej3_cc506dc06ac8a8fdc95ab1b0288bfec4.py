def decodificar(mensaje):
    # Dividir el mensaje en números binarios
    numeros_binarios = mensaje.split(",")

    # Convertir cada número binario a su equivalente decimal
    numeros_decimales = [int(binario, 2) for binario in numeros_binarios]

    # Convertir los números decimales en letras usando la función chr
    letras = [chr(decimal) for decimal in numeros_decimales]

    # Unir las letras y retornar el resultado
    mensaje_decodificado = "".join(letras)
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje_codificado = "01101000,01101111,01101100,01100001"
    resultado = decodificar(mensaje_codificado)
    print(resultado)
         