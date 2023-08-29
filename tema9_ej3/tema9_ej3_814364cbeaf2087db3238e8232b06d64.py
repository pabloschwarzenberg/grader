def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    numeros_decimales = [int(num_bin, 2) for num_bin in numeros_binarios]
    letras = [chr(num_dec) for num_dec in numeros_decimales]
    mensaje_decodificado = ''.join(letras)
    return mensaje_decodificado


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)

         