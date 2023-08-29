def jerigonzo(palabra):
  i = ""
  for letras in palabra:
    if letras in "AEIOUaeiouáéíóú": 
      i += letras
      i += "p"
    i += letras
  return i