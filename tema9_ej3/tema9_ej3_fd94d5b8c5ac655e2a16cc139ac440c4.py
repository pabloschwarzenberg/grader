def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    caracteres = [chr(int(binario, 2)) for binario in numeros_binarios]
    mensaje_decodificado = ''.join(caracteres)
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje_codificado = "01101000,01101111,01101100,01100001"
    mensaje_decodificado = decodificar(mensaje_codificado)
    print(mensaje_decodificado)
