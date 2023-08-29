def decodificar(mensaje):
    words = mensaje.split(",")
    message = ""
    for w in words:
      message += w
    return ''.join(chr(int(message[i*8:i*8+8],2)) for i in range(len(message)//8))

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         