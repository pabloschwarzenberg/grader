# completa el código de la funcióndef amigos(a, b):
def amigos(a,b):
  bandera = True 
  contador = 1
  acumulado1 = 0 
  acumulado2 = 0
  while contador<a: 
    if(a%contador) == 0:
      acumulado1 = acumulado1 + contador 
    contador = contador + 1
  contador = 1
  while contador <b:
    if (b%contador) == 0:
      acumulado2 = acumulado2 + contador 
    contador = contador + 1
    
  if a == acumulado2 and b == acumulado1:
    bandera = True 
  else:
    bandera = False 
  return bandera