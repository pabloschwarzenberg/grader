# por favor escribe aquí tu función
def es_primo(n):
  if n<2:
   return False
  elif n==2:
    return True
  else:
     for m in range(2,n):
       if n%m==0:
         return False
       elif m==n-1:
         return True
           