# completa el código de la función
def suma_divisores(a):
  i=1
  suma=0
  while i<=a:
     d=a%i
     if d==0:
       suma=suma+i
       i+=1
     else:
       suma=suma
       i+=1
  sumaf=suma-a
  if sumaf==1:
    return sumaf,True
  else:
    return sumaf,False