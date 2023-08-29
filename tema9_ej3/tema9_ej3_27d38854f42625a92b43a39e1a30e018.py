def decodificar(mensaje):
  a=mensaje.split(",")
  L=""
  for i in a:
    L+=chr(int(i[:8], 2))
  return L
  

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         