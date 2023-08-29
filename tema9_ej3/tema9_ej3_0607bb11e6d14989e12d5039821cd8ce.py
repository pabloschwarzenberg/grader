def decodificar(mensaje):
  M=mensaje.split(",")
  Mf="" 
  for p in M:
    C=chr(int(str(p),2))
    Mf=Mf+C 
  return Mf

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         