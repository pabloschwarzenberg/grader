# completa el código de la función
def suma_divisores(a):
  divisores = []
  contar = 0
  for i in range(1 , a): 
    if a % i == 0: 
      divisores.append(i) 
      contar += 1 
  if contar == 1: 
    return sum(divisores), True
  else:
    return sum(divisores), False
           