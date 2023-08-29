# completa el código de la función
def suma_divisores(a):
  suma_divisores = 0
  contador = 1
  primo = False
  
  while contador < a:
    if (a % contador) == 0:
      suma_divisores = suma_divisores + contador
    contador = contador + 1
  if suma_divisores == 1:
    primo = True 
    
  return suma_divisores, primo          