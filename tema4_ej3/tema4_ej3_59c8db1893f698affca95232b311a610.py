def jerigonzo(palabra):
 vocales = ['a', 'e', 'i', 'o', 'u']
 j = ''
 for letra in palabra:
   j += letra
   if letra.lower() in vocales:
     j += "p" + letra
 return j

        