def suma_divisores(x):
  divisores=0
  div=1
  suma_d=0
  while div<x:
    if x%div==0:
      suma_d=suma_d+div
      divisores=divisores+1
      div=div+1
    elif x%div!=0:
      div=div+1
  if suma_d==1:
    return suma_d,True
  else:
    return suma_d,False