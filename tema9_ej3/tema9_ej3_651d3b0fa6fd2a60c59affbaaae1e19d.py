def decodificar(mensaje):
  #KheVergha esto no es objetos
  mensaje=mensaje.split(",")
  i=0
  l=[]
  while i<len(mensaje):
    letrita= int(str(mensaje[i]),2)
    letrita=chr(int(letrita))
    l.append(letrita)
    i=i+1
  mensaje="".join(l)
  return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         