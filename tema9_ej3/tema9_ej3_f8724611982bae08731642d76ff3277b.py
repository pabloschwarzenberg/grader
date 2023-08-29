def decodificar(mensaje):
  a=0
  letras=""
  numero_uni=0
  while a<(len(mensaje)-1):
    numero=mensaje[a:a+8]
    
    x=numero[::-1]
    
    numero_uni=0
    for i in range(0,len(x)):
      if x[i]=="1":
        k=2**i
       
        numero_uni+=k
        
    letra1=str(chr(numero_uni))
      
    letras+=letra1
        
    a+=9
  return letras



if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         