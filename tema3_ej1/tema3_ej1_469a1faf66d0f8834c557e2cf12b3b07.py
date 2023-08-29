# completa el código de la función
def suma_divisores(a):
  divisores = []
  for i in range(1, a): 
      if a % i == 0:
          divisores.append(i)
  if(sum(divisores) != 1):
      return sum(divisores), False
  else:
      return sum(divisores), True