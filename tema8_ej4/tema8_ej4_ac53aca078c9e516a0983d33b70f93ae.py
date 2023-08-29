
def rot13(palabra):
  n = "abcdefghijklmnopqrstuvwxyz"
  resultado = ""
  for caracter in palabra:
    resultado += n[(n.find(caracter)+13)%26]
  return resultado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)