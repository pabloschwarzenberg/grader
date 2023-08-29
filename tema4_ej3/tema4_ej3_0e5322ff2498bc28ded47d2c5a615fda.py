def jerigonzo(string):
  x=""
  vocales="AEIOUaeiou"
  letras=("QWRTYPSDFGHJKLÑZXCVBNMqwrtypsdfghjklñzxcvbnm")
  espacio=" "
  for i in string:
    if i in letras:
      x+=i
    elif i in vocales:
      x+=i
      x+="p"
      x+=i
    elif i in espacio:
      x=x+i
  return x