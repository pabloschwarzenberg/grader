def jerigonzo(palabra):
  jerigonza = ""
  for letra in palabra:
    jerigonza += letra
    if letra in "AEUOUaeiou":
         # agregar p despues de la vocal
         jerigonza += "p"
         # repetir la vocal
         jerigonza += letra
  return (jerigonza)
  pass