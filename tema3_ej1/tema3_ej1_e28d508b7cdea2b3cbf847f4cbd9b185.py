# completa el código de la función
def suma_divisores(a):
  d=1
  suma=0
  while d<a :
    if a%d== 0:
      suma=suma+d
    d+=1
  if suma==1:
    return suma, True
  else :
    return suma, False