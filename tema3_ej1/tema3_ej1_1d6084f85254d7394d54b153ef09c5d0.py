# completa el código de la función
def suma_divisores(a):
  contador = 0
  for divisor in range(1,a-1):
    if (a % divisor) == 0 :
      contador += divisor
  print(contador)    
  if contador==1:
    primo = True
  else:
    primo = False

  return contador, primo
  

           