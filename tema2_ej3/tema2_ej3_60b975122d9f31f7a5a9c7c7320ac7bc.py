def numero_perfecto(a):
  adicion_divisores = 0
  contador = 1
  perfecto = False 
  while contador<a:
     if (a%contador) == 0:
       adicion_divisores = adicion_divisores + contador 
     contador = contador + 1 
  if adicion_divisores == a:
     perfecto = True 
  return perfecto
           