def suma_divisores(a):
  suma = 0
  for n in range(1, a):
    if a % n == 0:
      suma += n
    if suma==1:
      return(suma,True)
    elif suma!=1:
      return(suma,False)