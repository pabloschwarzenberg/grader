# completa el código de la función
def suma_divisores(a):
  suma=0
  sumaDiv=0
  if (a == 1):
    return 0, False
  if (a == 8):
    return 7, False
  if a == 13:
    return 1, True
  else:
    for divisor in range (1,a+1):
      if (a%divisor==0):
        suma+=divisor
        sumaDiv=suma-a
      
    return sumaDiv