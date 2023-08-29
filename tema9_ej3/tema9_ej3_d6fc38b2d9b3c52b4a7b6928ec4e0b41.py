def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = [chr(int(binario, 2)) for binario in numeros_binarios]
    mensaje_descifrado = ''.join(letras)
    return mensaje_descifrado

def main():
    mensaje_codificado = input("Ingrese el mensaje codificado: ")
    mensaje_descifrado = decodificar(mensaje_codificado)
    print("Mensaje descifrado:", mensaje_descifrado)

if __name__ == "__main__":
    main()

         