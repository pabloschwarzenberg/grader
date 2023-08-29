# completa el código de la función
def suma_divisores(a):
    i=1
    y=0
    while i<a:
        if a%i==0:
            y=i+y
        i=i+1
    if y==1:
        return (y,True)
    if y!=1:
        return (y,False)    
    if a<1:
        return (y,False)  
