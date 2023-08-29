# completa el código de la función
def suma_divisores(a):
  da=0
  for divisor in range(1,a):
        if a%divisor==0:
            da=da+divisor
  if da==1:
    return da,True
  else:
    return da,False
  

           