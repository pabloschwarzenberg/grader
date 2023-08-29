# completa el código de la función
def suma_divisores(n):
  a=0
  for i in range(1,n):
    if n%i==0:
      a+=i
  if a==1:
    return(a, True)
  else:
    return(a, False)
        

           