def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    mensaje_decodificado = ""
    for num_binario in numeros_binarios:
        num_decimal = int(num_binario, 2)  # Convertir binario a decimal
        letra = chr(num_decimal)  # Obtener la letra/símbolo correspondiente al código ASCII
        mensaje_decodificado += letra
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)

         