def rot13(palabra):
    L1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    L2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    L3=""
    c=0
    while c<len(palabra):
      d=0
      while d<13 :
        if L1[d]==palabra[c] :
            L3=L3+L2[d]
            break
        elif L2[d]==palabra[c] :
            L3=L3+L1[d]
            break
        else:
          d=d+1
      c=c+1
    return L3

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           