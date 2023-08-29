def rot13(palabra):
  L=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
  l=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
  Mensaje=""
  for i in range(len(palabra)):
    if palabra[i]==" ":
        Mensaje=Mensaje+" "
    else:
        for k in range(len(L)):
            if palabra[i]==L[k]:
                Mensaje=str(Mensaje)+str(l[k])
            elif palabra[i]==l[k]:
                Mensaje=str(Mensaje)+str(L[k])
  return Mensaje
  pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           