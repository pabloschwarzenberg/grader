def jerigonzo(string):
  vocales = ["a","e","i","o","u"]
  stringf = ""
  for letra in string:
    c = 0
    for vocal in vocales:
      if vocal == letra:
        letra += "p" + letra
      if vocal != letra:
        c += 1
    if c != 0:
      stringf += letra
    else:
      stringf += letra
  return(stringf)
         