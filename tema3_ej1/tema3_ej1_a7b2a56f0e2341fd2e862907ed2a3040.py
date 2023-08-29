# completa el código de la función
def suma_divisores(n):
    s=0
    for d in range (1,n):
        if n==1:
           s=0
        elif n%d==0:
            s=s+d
            
    if s > 1 or s==0:
      return ((s), False)
    else:
      return ((s), True)


