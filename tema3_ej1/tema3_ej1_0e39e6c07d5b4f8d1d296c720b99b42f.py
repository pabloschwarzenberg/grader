# completa el código de la función
def suma_divisores(a):
    b=0
    for n in range(1,a):
       if a%n==0:
          b=b+n
    if b==1:
       return(b,True)
    else:
        return(b,False)
  
           