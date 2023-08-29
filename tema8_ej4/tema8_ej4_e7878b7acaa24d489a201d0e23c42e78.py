def rot13(palabra):
    lista1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    lista2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    contador=0
    encriptado=[]
    while contador<len(palabra):
      contador2=0
      while contador2<len(lista1):
        if palabra[contador]==lista1[contador2]:
          encriptado.append(lista2[contador2])  
        if palabra[contador]==lista2[contador2]:
          encriptado.append(lista1[contador2])
        contador2+=1
      contador+=1
    encriptado="".join(encriptado)
    return encriptado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           