def decodificar(mensaje):
    # Dividir el mensaje en una lista de números binarios
    numeros_binarios = mensaje.split(",")

    # Convertir cada número binario a decimal y luego a su respectivo carácter ASCII
    caracteres = [chr(int(numero_binario, 2)) for numero_binario in numeros_binarios]

    # Unir los caracteres en una cadena y retornarla
    mensaje_decodificado = "".join(caracteres)
    return mensaje_decodificado


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
