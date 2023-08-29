def decodificar(mensaje):
    return mensaje
def decodificar(mensaje):
    # Separar los números binarios y convertirlos a decimales
    numeros_binarios = mensaje.split(',')
    decimales = [int(binario, 2) for binario in numeros_binarios]

    # Convertir los decimales en letras usando la función chr
    letras = [chr(decimal) for decimal in decimales]

    # Unir las letras y retornar el resultado
    resultado = ''.join(letras)
    return resultado

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         