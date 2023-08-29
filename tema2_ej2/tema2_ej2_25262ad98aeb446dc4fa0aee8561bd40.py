# completa el código de la función
def amigos(a,b):
  divisores_a = [1]
  divisores_b = [1]
  
  for i in range(2,a):
    if (a%i == 0):
      divisores_a.append(i)
  
  for i in range(2,b):
    if (b%i == 0):
      divisores_b.append(i)
  
  if (sum(divisores_a) == b) and (sum(divisores_b) == a):
    return True
  
  
  return False
           