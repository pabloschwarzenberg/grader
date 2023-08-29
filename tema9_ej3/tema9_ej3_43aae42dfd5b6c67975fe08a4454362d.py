def decodificar(mensaje):
    mensaje=list(mensaje)
    x=[]
    z=[]
    i=0
    while i<len(mensaje):
        if mensaje[i]!=",":
            x.append(mensaje[i])
            if i==len(mensaje)-1:
                numero="".join(x)
                largo=len(numero)
                d=0
                entero=0
                while d<largo:
                    potencia=2**(largo-d-1)
                    digito=int(numero[d])
                    entero=entero+digito*potencia
                    d+=1
                z.append(entero)
                x.clear()
                i+=1
                break
            i+=1
        if mensaje[i]==",":
            numero="".join(x)
            largo=len(numero)
            d=0
            entero=0
            while d<largo:
                potencia=2**(largo-d-1)
                digito=int(numero[d])
                entero=entero+digito*potencia
                d+=1
            z.append(entero)
            x.clear()
            i+=1
    mensaje.clear()
    for u in z:
      if u==" ":
        mensaje.append(u)
      if u!=" ":
        w=chr(u)
        mensaje.append(w)
    mensaje="".join(mensaje)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         