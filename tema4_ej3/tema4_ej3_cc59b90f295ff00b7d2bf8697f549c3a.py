
def jerigonzo(string):
  traslado = ""
  for letra in string:
    if letra in "AEIOUaeiou":
      traslado += letra
      traslado += "p"
    traslado += letra

  return traslado

if __name__ == "__main__":
  string = input("ingrese una palabra:")
  print(jerigonzo(string))