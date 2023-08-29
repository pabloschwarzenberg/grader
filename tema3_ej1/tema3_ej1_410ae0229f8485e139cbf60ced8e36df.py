# completa el código de la función
def suma_divisores(n):
    a=n-1
    x=0
    if n==1:
        return 0,False
    else:
        while a>=1:
            if n%a==0:
                x+=a
            a-=1
        if x>1:
            return x,False
        else:
            return 1,True
    
           