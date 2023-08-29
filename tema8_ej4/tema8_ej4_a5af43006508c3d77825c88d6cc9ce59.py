def rot13(palabra):
  a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
  b = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
  c = palabra.maketrans(a,b)
  return palabra.translate(c)

if __name__=="__main__":
  palabra=input("Ingresa la palabra que quieras encriptar: ")
  palabra.lower()
  palabra.translate(rot13(palabra))
  resultado=rot13(palabra)
  print("El resultado es: ",resultado)
           