def jerigonzo(string):
  
  jerigonz= ""
  
  for letra in string:
    if letra in "AEIOUaeiou":
      jerigonz= jerigonz + letra
      jerigonz= jerigonz + "p"
    jerigonz= jerigonz + letra
  return jerigonz