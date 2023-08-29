def jerigonzo(palabra):
 vocales = ["a", "e", "i", "o", "u"]
 jeri = ""
 for letra in palabra:
   jeri += letra
   if letra.lower() in vocales:
     jeri += "p" + letra
 return jeri