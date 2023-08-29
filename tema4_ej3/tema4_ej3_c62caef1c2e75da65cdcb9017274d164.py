def jerigonzo(palabras):
  contar = ""
  for letras in palabras:
    if letras in "AEIOUaeiou": 
      contar += letras
      contar += "p"
    contar += letras
  return contar