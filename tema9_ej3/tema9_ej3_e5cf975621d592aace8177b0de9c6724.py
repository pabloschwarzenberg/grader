def decodificar(mensaje):
  a=mensaje[0:8]
  b=mensaje[10:17]
  c=mensaje[19:26]
  d=mensaje[27:35]
  lista=[a,b,c,d]
  palabra=""

  for _ in lista:
    dec=int(str(_),2) #de binario a decimal
    y=chr(dec)
    palabra=palabra+ str(y)

  return palabra

if __name__ == "__main__":
  mensaje=decodificar("01101000,01101111,01101100,01100001")
  print(mensaje)
