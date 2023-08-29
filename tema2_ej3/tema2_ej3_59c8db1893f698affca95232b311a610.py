def numero_perfecto(a):
  divisores=0
  div=1
  suma_d=0
  while div<a:
    if a%div==0:
      suma_d=suma_d+div
      divisores=divisores+1
      div=div+1
    elif a%div!=0:
      div=div+1
  if suma_d==a:
    return True
  else:
    return False
           