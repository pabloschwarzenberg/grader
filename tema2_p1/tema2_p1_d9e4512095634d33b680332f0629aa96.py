# por favor escribe aquí tu función
def es_primo(num):
 for n in range(1, num):
  if num % n == 0 or num % n == 1:
   return False
 return True
