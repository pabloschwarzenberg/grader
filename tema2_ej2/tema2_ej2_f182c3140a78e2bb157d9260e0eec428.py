# completa el código de la función
def amigos(a,b):
  flag = True
  contador = 1
  acum1 = 0
  acum2 = 0
    
  while contador < a:
    if (a % contador) == 0:
      acum1 = acum1 + contador
    contador = contador + 1
  contador = 1
  while contador < b:
    if (b % contador) == 0:
      acum2 = acum2 + contador
    contador = contador + 1
    
  if a == acum2 and b == acum1:
    flag = True
  else: 
    flag = False
  return flag
           