def jerigonzo(palabra):
  traduccion=""
  for letra in palabra:
    if letra in "AEIOUaeiou":
      traduccion+=letra
      traduccion+="p"
    traduccion+=letra
  return traduccion

if __name__ == "__main__":
  palabra=input("Ingrese una palabra: ")
  print(jerigonzo(palabra))