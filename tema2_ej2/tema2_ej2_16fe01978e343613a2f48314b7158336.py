# completa el código de la función
def amigos(a,b):
  d = 1
  suma = 0
  while d<a:
      if a%d == 0:
         suma = suma + d
      d = d + 1
  if suma == b:
         return True
  else:
         return False

      
           