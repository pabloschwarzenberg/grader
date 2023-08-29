def jerigonzo(string):
  mensaje=""
  vocales= "aeiou"
  consonantes= "bcdfghjklmnpqrstvwxyz"
  for n in string:
    if n in consonantes:
      mensaje += n
    if n in vocales:
      mensaje += n+"p"+n
    if n==" ":
      mensaje += " "
      
  return mensaje