def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = [chr(int(num_binario, 2)) for num_binario in numeros_binarios]
    mensaje_descifrado = ''.join(letras)
    return mensaje_descifrado
if __name__ == "__main__":
    mensaje = "01101000,01101111,01101100,01100001"
    mensaje_descifrado = decodificar(mensaje)
    print(mensaje_descifrado)