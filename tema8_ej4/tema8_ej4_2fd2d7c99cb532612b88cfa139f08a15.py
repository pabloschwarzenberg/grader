def rot13(palabra):
  abc="abcdefghijklmnopqrstuvwxyz"
  palabracifrada=""
  for i in palabra:
    suma=abc.find(i)+13
    indice=int(suma)%len(abc)
    palabracifrada=palabracifrada+str(abc[indice])
  return palabracifrada

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ").lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           