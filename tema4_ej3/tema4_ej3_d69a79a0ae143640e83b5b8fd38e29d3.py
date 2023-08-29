def jerigonzo(string):
     
     strAux =""
     ind = 0
     largo = len(string)
     vocales=["a","e","i","o","u"]
     for i in string:
      if(i in vocales):
         try:
             ca="p"
             strAux += string[ind]
             strAux += string[ind +1].replace(string[ind + 1], ca)
             if(largo != (ind + 1)):
                 ind += 1
        
             return strAux
     