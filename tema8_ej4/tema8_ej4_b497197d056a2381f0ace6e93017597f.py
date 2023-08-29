def rot13(palabra):
  final = ""
  for letra in palabra:
    for letra2 in abc:
      if letra == letra2 in abc:
        if abc.index(letra) > 12:
          final += abc[abc.index(letra) - 13]
        else:
          final += abc[abc.index(letra) + 13]
  return final    
    
    
abc = "abcdefghijklmnopqrstuvwxyz"  

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           