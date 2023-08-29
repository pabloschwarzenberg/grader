def jerigonzo(palabra):
  contador = ""
  for letra in palabra:
    if letra in "AEIOUaeiou": 
      contador += letra
      contador += "p"
    contador += letra
  return contador
if __name__ == "__main__":
  jerigonzo(input(str("ingrese una palabra:")))