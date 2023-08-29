def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")  # Separar los números binarios por comas
    caracteres = []

    for numero_binario in numeros_binarios:
        decimal = int(numero_binario, 2)  # Convertir el número binario a decimal
        caracter = chr(decimal)  # Obtener el caracter correspondiente al código ASCII decimal
        caracteres.append(caracter)

    mensaje_descifrado = "".join(caracteres)  # Unir todos los caracteres en un string

    return mensaje_descifrado

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)

         