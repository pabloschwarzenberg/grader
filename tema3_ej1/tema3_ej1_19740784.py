# completa el código de la función
def suma_divisores(a):
    b=0
    for i in range(1,a):
        if a%i==0:
            b+=i
    if b==1:
        return(b,True)
    else:
       return(b,False)


           