# completa el código de la función
def suma_divisores(a):
  d = []
  contador = 0
  for i in range(1 , a): 
    if a % i == 0: 
      d.append(i) 
      contador += 1 
  if contador == 1: 
    return sum(d), True
  else:
    return sum(d), False  