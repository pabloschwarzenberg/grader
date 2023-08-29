# completa el código de la función
def suma_divisores(a):
  suma_num = 0
  for indice in range(1, a-1):
    resto = a % indice
    if resto != 0:
      continue
    suma_num += indice
  if suma_num == 1:
    primo_boo = True
  else:
    primo_boo = False
  return suma_num, primo_boo
           
           