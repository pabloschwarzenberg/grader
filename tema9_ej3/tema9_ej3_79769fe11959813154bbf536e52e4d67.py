def decodificar(mensaje):
  letra1 = "01101000"
  letra2 = "01101111"
  letra3 = "01101100"
  letra4 = "01100001"
  codAscii1 = int(letra1,2)

  codAscii2 = int(letra2,2)

  codAscii3 = int(letra3,2)

  codAscii4 = int(letra4,2)

  mensaje = chr(codAscii1),chr(codAscii2),chr(codAscii3),chr(codAscii4)
  mensaje = "".join(mensaje)
  return mensaje
    

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         