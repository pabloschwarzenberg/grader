def decodificar(mensaje):
    mensaje=mensaje.split(",")
    num=[]
    pal=[]
    for j in mensaje:
      n=0
      la=len(j)
      for i in range(len(j)):
        if j[i]=="1":
          n=n+(2**(la-i-1))
      num.append(n)
    for k in num:
      pal.append(chr(k))
    mensaje="".join(pal)
    
    return mensaje
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)

         
