def rot13(palabra):
    i=0
    alfa=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    palabra=list(palabra)
    while i<len(palabra):
      if alfa.index(palabra[i])<13:
        palabra[i]=alfa[alfa.index(palabra[i])+13]
        i+=1
      else:
        palabra[i]=alfa[alfa.index(palabra[i])-13]
        i+=1
    palabra="".join(palabra)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    print("El resultado es: ",rot13(palabra))
           