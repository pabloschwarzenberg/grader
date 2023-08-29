# completa el código de la función
def suma_divisores(a):
  x=1
  z=0
  while(x<a):
    j=a%x
    if(j==0):
      z=z+x      
      x=x+1
    else:
      x=x+1
  if(z==1):
    c=True
    return (z,c)
  else:
    c=False
    return (z,c)


