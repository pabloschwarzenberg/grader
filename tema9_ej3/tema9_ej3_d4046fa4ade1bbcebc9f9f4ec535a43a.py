def decodificar(mensaje):
    # Dividir el mensaje en una lista de números binarios
    numeros_binarios = mensaje.split(',')

    # Convertir cada número binario a su equivalente decimal y luego a su carácter ASCII
    caracteres = [chr(int(binario, 2)) for binario in numeros_binarios]

    # Unir los caracteres para formar el mensaje descifrado
    mensaje_descifrado = ''.join(caracteres)

    return mensaje_descifrado


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
