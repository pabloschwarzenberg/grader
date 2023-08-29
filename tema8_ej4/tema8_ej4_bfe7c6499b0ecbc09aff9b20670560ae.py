def rot13(palabra):
  n = "abcdefghijklmmnopqrstuvwxyz"
  resultado = ""
  for caracter in palabra:
    resultado += n[(n.find(caracter)+13)%26]
  return resultado
  
 if __name__=="__main__":
     palabra=input("palabra: ")
     palabra.lower()
      resultado=rot13(palabra)
      print("el resultado: ",resultdo)
           