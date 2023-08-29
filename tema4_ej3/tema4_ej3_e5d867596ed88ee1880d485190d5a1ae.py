def jerigonzo (string):
     idioma=""
     for abc in string:
#        print("entrada_1")
         if abc in "aeiouAEIOU":
              idioma +=abc
              idioma +="p"
#              print(idioma)
#              print("entrada")
         idioma+=abc
     return(idioma)