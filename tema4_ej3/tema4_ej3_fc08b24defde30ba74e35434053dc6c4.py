def jerigonzo(string):
  contador = ""
  for letra in string:
    if letra in "AEIOUaeiou": 
      contador += letra
      contador += "p"
    contador += letra
  return contador

         