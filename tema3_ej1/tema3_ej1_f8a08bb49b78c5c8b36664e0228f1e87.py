# completa el código de la función
def suma_divisores(n):
  divisores= []
  
  for i in range(1, n):
    if n % i ==0:
      divisores.append(i)
      
  if sum(divisores)==0:
    return sum(divisores), False
  elif (sum(divisores) % 2 ==0) or (sum(divisores) ==1):
    return sum(divisores), True
  else:
    return sum(divisores), False
  
  
           