def jerigonzo(string):
     doblao=""
     for letra in string:

         if letra in "aeiouAEIOU":
              doblao +=letra
              doblao +="p"
         doblao+=letra
     return doblao