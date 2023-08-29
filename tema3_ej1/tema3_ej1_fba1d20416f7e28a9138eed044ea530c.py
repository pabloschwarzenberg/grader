# completa el código de la función
def suma_divisores(a):
  divisores = [i for i in range(1, a+1) if a % i == 0]
  primo = False
  if a!=1:
    if len(divisores) == 2:
      primo = True
    else:
      primo = False
  return (sum(divisores)-a), primo