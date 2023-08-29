def decodificar(mensaje):
  x = mensaje.split(",")
  string = ""
  for binario in x:
    string  = string + chr(int(binario,2))

  return string

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         