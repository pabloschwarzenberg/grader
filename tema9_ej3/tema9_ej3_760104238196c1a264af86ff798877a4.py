def decodificar(mensaje):
    return ''.join(chr(int(i, 2)) for i in mensaje.split(','))

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         