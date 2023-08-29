def rot13(texto):
  fila1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
  fila2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]

  nuevo=""

  for i in texto:

    if i in fila1:
      y=fila1.index(i)
      j=fila2[y]
      nuevo+=j
               
               


    elif i in fila2:
       y=fila2.index(i)
       j=fila1[y]
       nuevo+=j
          


               
  return nuevo


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           