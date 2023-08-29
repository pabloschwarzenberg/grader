def rot13(palabra):
  desplazamiento=13
  cambio=""
  if palabra==palabra.isupper:
    abecedario="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  else:
    abecedario="abcdefghijklmnopqrstuvwxyz"
  for i in palabra:
    if i in abecedario:
      x=(abecedario.index(i)+desplazamiento)
      y=(len(abecedario))
      cambio+=abecedario[x % y]
    else:
      cambio+=i
  if len(cambio)==len(palabra):
    return cambio
    
if __name__=="__main__":
  palabra=input("Ingresa la palabra que quieras encriptar: ")
  palabra.lower()
  resultado=rot13(palabra)
  print("El resultado es: ",resultado)