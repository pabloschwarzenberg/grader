# completa el código de la función
def suma_divisores(a):
  divisores = []
  for i in range(a-1):
    if a%(i+1) == 0:
      divisores.append(i+1)
  if len(divisores) != 1:
    return (sum(divisores),False)
  else:
    return (sum(divisores),True)
           