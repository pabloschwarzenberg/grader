def decodificar(mensaje):
    mensaje = mensaje.split(',')
    palabra = ''
    for i in mensaje:
        palabra += chr(int(i, 2))
        
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         