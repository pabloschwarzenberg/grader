def jerigonzo(string):
  palabra = ""
  for letra in string.lower():
    if letra in "aeiouáéíóúü":
      palabra += letra
      palabra += "p"
    palabra += letra
  
  return palabra


         