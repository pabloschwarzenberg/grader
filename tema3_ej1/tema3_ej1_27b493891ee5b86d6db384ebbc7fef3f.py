# completa el código de la función
def suma_divisores(a):
  sumadiv = 0
  for i in range(1,a):
    if a % i == 0:
      #i es divisor
      sumadiv = sumadiv + i
      print(sumadiv)
  #return sumadiv
  if sumadiv == 1:
    return sumadiv,True
  else:
    return sumadiv,False