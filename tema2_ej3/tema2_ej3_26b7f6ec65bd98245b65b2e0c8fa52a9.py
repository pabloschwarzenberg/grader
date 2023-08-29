def numero_perfecto(a):
  divisores=[]
  divisor=1
  while divisor<a:
    if a%divisor==0:
      divisores.append(divisor)
    divisor=divisor+1
  i=0
  suma=0
  for i in divisores:
    suma=i+suma
    print(suma)
    i=i+1
  if suma==a:
    return True
  else:
    return False