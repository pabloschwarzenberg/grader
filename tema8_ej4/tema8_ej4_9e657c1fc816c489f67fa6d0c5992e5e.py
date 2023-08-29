def rot13(palabra):
  a1 = "abcdefghijklm"
  a2 = "nopqrstuvwxyz"

  coded = ""
  j = 0
  for i in palabra:
      char = palabra[j]
      if char in a1:
          char = a2[a1.index(char)]
        
      elif char in a2:
          char = a1[a2.index(char)]
        
      j += 1
      coded += char
    
  return coded

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           