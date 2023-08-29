def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    caracteres = [chr(int(num_binario, 2)) for num_binario in numeros_binarios]
    mensaje_decodificado = ''.join(caracteres)
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje = "01101000,01101111,01101100,01100001"
    mensaje_decodificado = decodificar(mensaje)
    print(mensaje_decodificado)
