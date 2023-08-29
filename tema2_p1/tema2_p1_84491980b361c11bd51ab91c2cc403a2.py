# por favor escribe aquí tu función
def es_primo(a):
 i=2 
 if a==1:
  return False
 while i<a:
  if a%i==0:
   return False
  i=i+1
 return True