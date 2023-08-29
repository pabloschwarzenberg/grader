def jerigonzo(string):
  palabra_original = str(string)
  vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
  palabra_final=""
  for letra in palabra_original:
    if letra not in vocales :
      palabra_final += letra
    else:
      palabra_final += letra + "p" + letra
  return palabra_final


         