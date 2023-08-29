def numero_perfecto(a):
  suma_div=0
  for i in range (1,a):
    if a%i==0:
      suma_div += (i)
  if suma_div==a:
    return True
  else:
    return False