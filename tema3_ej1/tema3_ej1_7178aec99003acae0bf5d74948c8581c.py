# completa el código de la función
def suma_divisores(a):
  t=0
  if a!=1:
    for i in range(1,a):
      if (a%i==0):
        t=t+i
    if t==1:
      return(t, True)
    else:
      return(t, False)
  if a==1:
    return(t, False)