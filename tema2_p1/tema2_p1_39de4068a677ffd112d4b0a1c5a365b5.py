# por favor escribe aquí tu función
def es_primo(num):
   if num<2:
      return False
   for i in range(2,(num//2)+1):
      if num%i==0:
         return False
   return True