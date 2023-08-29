# por favor escribe aquí tu función
def es_primo(p):
   if p > 1:
       for i in range(2,p):
           if p % i == 0:
               return False
           return True
   else:
     return False
           