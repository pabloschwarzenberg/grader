# completa el código de la función
def suma_divisores(a):
    x=0
    if a!=1:
      for k in range(1,a):
          if (a%k)==0:
              x=x+k
    if x==1:
      return x,True
    else:
      return x,False
  
           