def jerigonzo(string):
 traducido = ""
 for palabra in string:
  traducido += palabra
  if palabra.lower() in "aeiou":
    traducido += "p" + palabra
 return traducido