def jerigonzo(string):
    mensaje= ""
    vocales= "aeiou"
    consonantes="bcdfghjklmnpqrstvwxyz"
    for i in string:
      if i in consonantes:
        mensaje+=i
      if i in vocales:
        mensaje +=i+"p"+i
      if i==" ":
        mensaje+=" "
    return mensaje


         