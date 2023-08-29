# completa el código de la función
def suma_divisores(a):
  div1=a-1
  sumdiv=0
  if a==1:
      sumdiv=0
  if a!=1:
      while div1!=0:
          if a%div1==0:
              divisor=div1
              sumdiv=sumdiv+divisor
          div1=div1-1
  if sumdiv==1:
      ej=True
  else:
      ej=False
  return (sumdiv,ej)
           