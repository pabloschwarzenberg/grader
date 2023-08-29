def jerigonzo(string):
  pal = ""
  voc = ["A","a","E","e", "I", "i", "O", "o", "U", "u"]
  for b in string:
    if b in voc:
      pal += b
      pal += "p"
    pal += b
    pass
  return pal
