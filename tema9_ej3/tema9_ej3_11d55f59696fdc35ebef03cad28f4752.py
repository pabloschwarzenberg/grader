def decodificar(mensaje):
  xd = mensaje
  xd = xd.split(sep = ",")
  lol = []
  olo = []
  for x in xd:
    af = int(x, 2)
    lol.append(af)
  for x in lol:
    aux = chr(x)
    olo.append(aux)
  return "".join(olo)
 

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         