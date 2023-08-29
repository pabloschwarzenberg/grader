# por favor escribe aquí tu función
def es_primo(numero):
  divisores=0
  div=1
  while div<=numero:
   if numero%div==0:
    divisores=divisores+1
    div=div+1
   elif numero%div!=0:
    div=div+1
  if divisores==2:
   return True
  else: 
   return False
           