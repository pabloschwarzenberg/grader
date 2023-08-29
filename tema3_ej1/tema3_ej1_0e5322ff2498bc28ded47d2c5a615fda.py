# completa el código de la función
def suma_divisores(a):
  y = 0
  while a > 0:
    if a==1:
      return False
    else:
      x=a-1
      division=(a % x)
      if division != 0:
        y= y + division
    print(y)
    if y==1:
      return True
    else:
      return False