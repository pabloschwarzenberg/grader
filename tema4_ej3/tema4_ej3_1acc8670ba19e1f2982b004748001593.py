def jerigonzo(string):
  palabra = ""
  vocales = ["A","a","E","e", "I", "i", "O", "o", "U", "u"]
  for letra in string:
    if letra in vocales:
      palabra += letra
      palabra += "p"
    palabra += letra

  return palabra

if __name__ == "__main__":
    pass
         