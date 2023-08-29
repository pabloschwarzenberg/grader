def jerigonzo(aleluya):
  contador = ""
  for letra in aleluya:
    if letra in "AEIOUaeiou": 
      contador += letra
      contador += "p"
    contador += letra
  return contador
         