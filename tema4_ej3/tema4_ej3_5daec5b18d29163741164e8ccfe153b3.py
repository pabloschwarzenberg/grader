def jerigonzo(string):
  termino = ""
  vocales = ["A","a","E","e", "I", "i", "O", "o", "U", "u"]
  for letra in string:
    if letra in vocales:
      termino += letra
      termino += "p"
    termino += letra

  return termino