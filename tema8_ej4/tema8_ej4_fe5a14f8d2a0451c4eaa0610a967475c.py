
abcdario='abcdefghijklmnopqrstuvwxyz'

def rot13(palabra):
  global abcdario
  plbrot13=''
  for i in range(len(palabra)):
    x=palabra[i]
    y=abcdario.find(x)
    if y<13:
     plbrot13+=abcdario[y+13]
    if y>12:
     plbrot13+=abcdario[y-13]
  return plbrot13
###############################
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)