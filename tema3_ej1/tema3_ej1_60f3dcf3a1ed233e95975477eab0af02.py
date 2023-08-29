# completa el código de la función
def suma_divisores(a):
  divisores = [1]

  for i in range(2,a + 1):
    if a % i == 0:
      divisores.append(i)

    if sum(divisores) == (a + 1):
      return (True +","+len(str(divisores))
    elif sum(divisores) == 1:
      return(False,0)
    else:
      return (False +","+len(str(divisores))