def jerigonzo(string):
  palabra = ""
  vocales = ["a" , "e" , "i" , "o" , "u"]
  for letra in string:
    if letra in vocales:
      palabra = palabra + letra
      palabra = palabra + "p"
    palabra = palabra + letra

  return palabra
         