def rot13(palabra):
    u=len(palabra)
    i=int
    i=0
    a=[]
    while i<u:
      final=ord("z")
      inicio=ord("a")
      if (ord(palabra[i])+13)>final:
        b=inicio-final+ord(palabra[i])+12
        a.append(chr(b))
      else:
        a.append(chr(ord(palabra[i])+13))
      i=i+1
    palabra="".join(a)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           