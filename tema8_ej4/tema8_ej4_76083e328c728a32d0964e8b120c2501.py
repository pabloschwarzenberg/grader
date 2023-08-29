def rot13(palabra):
  lista1=["a","b","c","d","e","f","g","h","i","j","k","l","m",""]
  lista2=["n","o","p","q","r","s","t","u","v","w","x","y","z",""]
  palabra2=""
  for i in palabra:
    if i in lista1:
      posicion = lista1.index(i)
      letranueva = lista2[posicion]
      palabra2 = palabra2+letranueva
    else:
      posicion = lista2.index(i)
      letranueva = lista1[posicion]
      palabra2 = palabra2 + letranueva
  return palabra2    
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           