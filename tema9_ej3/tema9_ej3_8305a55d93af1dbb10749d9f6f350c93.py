def decodificar(mensaje):
  mensaje=bin(mensaje)
  mensaje=chr(mensaje)
  mensaje=ord(mensaje)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         