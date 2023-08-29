def jerigonzo(palabra):
  i = ""
  for letter in palabra:
    if letter in "AEIOUaeiouáéíóú": 
      i += letter
      i += "p"
    i += letter
  return i         