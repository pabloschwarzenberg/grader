def jerigonzo(string):
  word = ""
  vocal = ["A","E","I","O","U","a","e","i","o","u"]
  for letra in string:
    if letra in vocal:
      word += letra
      word += "p"
    word += letra

  return word