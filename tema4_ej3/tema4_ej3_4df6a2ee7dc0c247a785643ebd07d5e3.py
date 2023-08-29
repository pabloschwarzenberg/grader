def jerigonzo(string):
  aux = ""
  for i in string:
    if i in ("a", "e", "i","o","u"):
      aux = aux + i + "p"+i
    else:
      aux = aux + i
  return aux        