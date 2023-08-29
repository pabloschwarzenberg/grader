def decodificar(mensaje):
    # Dividir el mensaje en una lista de números binarios
    numeros_binarios = mensaje.split(",")

    # Convertir cada número binario a su equivalente decimal y luego a la letra correspondiente
    letras = [chr(int(binario, 2)) for binario in numeros_binarios]

    # Unir las letras en un solo string
    mensaje_decodificado = "".join(letras)

    return mensaje_decodificado

if __name__ == "__main__":
    mensaje_codificado = input("Ingrese el mensaje codificado: ")
    mensaje_decodificado = decodificar(mensaje_codificado)
    print("Mensaje decodificado:", mensaje_decodificado)