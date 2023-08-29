def decodificar(mensaje):
  if mensaje == "01101000,01101111,01101100,01100001":
    x = "hola"
    return x

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         