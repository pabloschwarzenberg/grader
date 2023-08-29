# completa el código de la función
def suma_divisores(a):
  divisores= []
  b=0
  for i in range(1,a):
    if a % i == 0:
     divisores.append(i)
    if sum(divisores) == 1:
      b=True
    else:
      b= False
  return (sum(divisores),b)

           