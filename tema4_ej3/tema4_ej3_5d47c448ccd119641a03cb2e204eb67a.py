def jerigonzo(string):
     translation=""
     for letra in string:
#        print(" la entrada es 1")
         if letra in "aeiouAEIOU":
              translation +=letra
              translation +="p"
#              print(translation)
#              print("es ingresada")
         translation+=letra
     return(translation)