def rot13(palabra):
  res=''
  a='abcdefghijklmnopqrstuvwxyz'
  for i in palabra:
    res+=a[(a.find(i)+13)%26]
  return res

if __name__=="__main__":
  palabra=input("Ingresa la palabra que quieras encriptar: ")
  palabra.lower()
  resultado=rot13(palabra)
  print("El resultado es: ",resultado)