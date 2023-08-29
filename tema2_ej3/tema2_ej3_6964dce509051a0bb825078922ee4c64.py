def numero_perfecto(numero):
  suma=0
  for i in range(1,numero):
    if numero%1==0:
      suma+=i
  return suma == numero


           