def jerigonzo(string):
  Palabra = ""
  Vocales = ["A","a","E","e", "I", "i", "O", "o", "U", "u"]
  for Letra in string:
    if Letra in Vocales:
      Palabra += Letra
      Palabra += "p"
    Palabra += Letra

  return Palabra
         