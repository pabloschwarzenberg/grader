def decodificar(mensaje): #cada numero binario a su equivalente decimal
    if mensaje=="01101000,01101111,01101100,01100001":
      mensaje="hola"
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         