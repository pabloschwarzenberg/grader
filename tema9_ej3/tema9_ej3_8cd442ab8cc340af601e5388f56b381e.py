def decodificar(mensaje):
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = [chr(int(numero_binario, 2)) for numero_binario in numeros_binarios]
    mensaje_descifrado = ''.join(letras)
    return mensaje_descifrado