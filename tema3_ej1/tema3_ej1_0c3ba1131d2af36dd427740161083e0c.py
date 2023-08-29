# completa el código de la función
def suma_divisores(a):
    b=0
    j=0
    while(b<a):
        b=b+1
        if (a == b):
            break
        if(a%b==0):
            j=j+b
    if(j==1):
          return(j,True)
    else:
         return(j,False)

           