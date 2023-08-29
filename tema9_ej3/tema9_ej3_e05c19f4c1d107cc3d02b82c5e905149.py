def decodificar(mensaje):
    mensaje = mensaje.split(',')
    for i, b in enumerate(mensaje):
        mensaje[i] = chr(int(b, 2))
    return ''.join(mensaje)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
