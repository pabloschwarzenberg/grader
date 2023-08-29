def jerigonzo(string):
   nueva_palabra = []
   for palabra in string:
       for letra in palabra:
           if letra in "aeiouAEIOU":
               letra = letra + "p"+ letra
           nueva_palabra.append(letra)
   nueva_palabra = "".join(nueva_palabra)
   return nueva_palabra


         