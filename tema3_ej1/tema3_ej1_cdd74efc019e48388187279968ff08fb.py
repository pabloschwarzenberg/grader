# completa el código de la función
def suma_divisores(n):
    c=0
    for a in range(1,n):
        if n%a==0:
            c=c+a
        if c==1:
          return print(c,True)
        else:
           return print(c,False)
