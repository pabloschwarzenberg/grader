def jerigonzo(string):
  frase = ""
  vocal = ["a","e","i","o","u"]
  for i in string:
    if i in vocal:
      frase += i
      frase += "p"
      frase += i 
    else:
      frase += i 
  return frase




