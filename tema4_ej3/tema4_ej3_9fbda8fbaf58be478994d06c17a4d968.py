def jerigonzo(string):
     traduccion=""
     for letra in string:
#        print("entra 1")
         if letra in "aeiouAEIOU":
              traduccion +=letra
              traduccion +="p"
#              print(traduccion)
#              print("entra")
         traduccion+=letra
     return(traduccion)
  
         