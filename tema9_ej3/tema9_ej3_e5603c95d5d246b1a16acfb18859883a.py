def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = []
    for numero_binario in numeros_binarios:
        numero_decimal = int(numero_binario, 2)
        letra = chr(numero_decimal)
        letras.append(letra)
    mensaje_decodificado = ''.join(letras)
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje_codificado = "01101000,01101111,01101100,01100001"
    mensaje_decodificado = decodificar(mensaje_codificado)
    print("Mensaje decodificado:", mensaje_decodificado)

         