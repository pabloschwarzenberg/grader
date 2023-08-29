def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = [chr(int(numero, 2)) for numero in numeros_binarios]
    mensaje_descifrado = ''.join(letras)
    return mensaje_descifrado

if __name__ == "__main__":
    mensaje_codificado = "01101000,01101111,01101100,01100001"
    mensaje_descifrado = decodificar(mensaje_codificado)
    print(mensaje_descifrado)
