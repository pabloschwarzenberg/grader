# completa el código de la función
def amigos(a,b):
    sa=suma(a)
    se=suma(b)
    if(sa==b and se==a):
        return True
    else:
        return False
    
def suma(n):
    s=0
    for i in range(1,n):
        if(n % i==0):
            s=s+i
            
    return s 
           