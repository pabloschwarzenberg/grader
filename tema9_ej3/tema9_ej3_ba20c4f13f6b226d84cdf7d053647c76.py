def decodificar(mensaje):
    # Separar los números binarios
    numeros_binarios = mensaje.split(',')

    # Convertir cada número binario a decimal y luego a su correspondiente carácter ASCII
    caracteres = [chr(int(binario, 2)) for binario in numeros_binarios]

    # Unir los caracteres y retornar el mensaje descifrado
    mensaje_descifrado = ''.join(caracteres)
    return mensaje_descifrado

if __name__ == "__main__":
    mensaje = "01101000,01101111,01101100,01100001"
    mensaje_descifrado = decodificar(mensaje)
    print(mensaje_descifrado)
