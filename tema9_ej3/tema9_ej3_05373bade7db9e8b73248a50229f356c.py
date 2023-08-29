def bin_a_dec(mensaje):
  mensaje=mensaje.split(",")
  mensaje=list(mensaje)
  decimales=[]
  suma=0
  for i in range(len(mensaje)):
    for j in range(8):
        if mensaje[i][j]=="1":
           numero=int(2**(8-(j+1)))
           suma+=numero
        else:
            suma+=0
    decimales.append(suma)
    suma=0
  return decimales
  
def decodificar(mensaje):
  decimales=bin_a_dec(mensaje)
  letras=[]
  for i in decimales:
    letra=chr(i)
    letras.append(letra)
  mensaje="".join(letras)
  return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         