def suma_divisores(a):
  suma=0
  for m in range(1,a):
    if a%m==0:
      suma=suma+m
  if suma==1:
    return(suma,True)
  else:
    return(suma,False)