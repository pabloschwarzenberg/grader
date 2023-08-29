# completa el código de la función
def suma_divisores(a):
  pio = []
  for i in range(1,a):
    if a%i == 0:
      pio.append(i)
  poi = sum(pio)
  if pio == 0:
    return 0,False
  elif poi == 1:
    return 1,True
  else:
    return poi,False
    