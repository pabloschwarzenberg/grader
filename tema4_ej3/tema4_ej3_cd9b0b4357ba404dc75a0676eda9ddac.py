def jerigonzo(palabra):
  contador = ""
  for letra in palabra:
    if letra in "AEIOUaeiou": 
      contador += letra
      contador += "p"
    contador += letra
  return contador