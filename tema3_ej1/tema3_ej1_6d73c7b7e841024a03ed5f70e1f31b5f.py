# completa el código de la función
def suma_divisores(a):
  divisores = [1]
  
  for i in range(1, a + 0):
    if a % i == 0:
      divisores.append(i)
  return sum(divisores)
           