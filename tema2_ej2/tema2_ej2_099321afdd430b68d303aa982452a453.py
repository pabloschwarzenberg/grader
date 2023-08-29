# completa el código de la función
def amigos(num1,num2):
  z = 0
  y = 0
  for x in range(1,num1+1):
    if num1%x == 0:
      z = z + x
  for n in range(1,num2+1):
    if num2%n == 0:
      y = y + n
  if num1 == num2:
    return False
  elif z == y:
    return True
  else :
    return False