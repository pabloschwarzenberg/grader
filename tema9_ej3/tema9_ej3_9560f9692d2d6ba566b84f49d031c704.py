def decodificar(mensaje):
    mensaje = mensaje.split(',')
    numeros = [int(x,2) for x in mensaje]
    caracteres = [chr(i) for i in numeros]
    return ''.join(caracteres)

if __name__ == '__main__':
    print(decodificar('01101000,01101111,01101100,01100001'))
    print(decodificar('10111111,01110001,01110101,11101001,00100000,01110100,01100001,01101100,00111111'))