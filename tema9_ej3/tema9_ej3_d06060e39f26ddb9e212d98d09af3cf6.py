def decodificar(mensaje):
  listaF=[]
  for x in (mensaje):
    if x!=",":
      letra= chr(int((x)))
      listaF.append(str(letra))
     
  cadena= "".join(listaF)
  cadena=ord(cadena)
    
   

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         