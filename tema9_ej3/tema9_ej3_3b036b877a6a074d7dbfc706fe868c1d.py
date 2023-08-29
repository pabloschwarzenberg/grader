def decodificar(mensaje):
  mensaje=mensaje.split(",")
  i=0
  j=len(mensaje)-1
  lista=[]
  while j>=i:
      a=(int(mensaje[i],2))
      agrega=chr(a)
      lista.append(agrega)
      i=i+1
  lista="".join(lista)
  return lista

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)