def jerigonzo(palabra):
  contador = ""
  for i in palabra:
    if i in "AEIOUaeiou": 
      contador += i
      contador += "p"
    contador += i
  return contador
