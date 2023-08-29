def rot13(palabra):
  cifrado = ""
  i = 0
  ALFABETO ="abcdefghijklmnopqrstuvwxyz"
  while i < len(palabra):
    if palabra[i] in ALFABETO:
      cifrado += ALFABETO[(ALFABETO.index(palabra[i])+13)%len(ALFABETO)]
    else:
      cifrado = cifrado+palabra[i]
    i+=1
  return cifrado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           