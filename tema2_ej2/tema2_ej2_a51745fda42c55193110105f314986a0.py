# completa el código de la función
def amigos(a,b):
   x = 1
   suma = 0
   while x < a:
      if a % x == 0:
         suma = suma + x

      x = x + 1

   if suma == b:
      return True
   else:
      return False