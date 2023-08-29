# completa el código de la función
def suma_divisores(a):
  divisores=[1]
  for i in range(2,a+1):
    if (a%i ==0 or a==1):
      divisores.append(i)
      if a <= 1:
        return (sum(divisores),False)
      elif a == 2:
        return (sum(divisores),True)
      else:
        for i in range(2, a):
          if a % i == 0:
            return (sum(divisores),False)
        return (sum(divisores),True) 
