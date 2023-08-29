# completa el código de la función
def suma_divisores(c):
  divisores=[]
  for a in range(1, c+1):
      if c % a == 0:
           divisores.append(a)
  suma=0
  for b in divisores:
      suma=suma+b
  suma=suma-divisores[-1]
  if suma==1:
     return(suma,True)
  else:
      return(suma,False)
           