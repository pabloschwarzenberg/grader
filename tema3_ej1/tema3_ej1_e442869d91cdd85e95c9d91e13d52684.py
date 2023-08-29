# completa el código de la función
def suma_divisores(a):
    z=[1]
    for x in range(2,a+1):
        if a%x==0:
            z.append(x)
    
    x=sum(z)
    x=x-a
    primo=True
    if x==1:
       primo=True
    else:
       primo=False
        
   
          
        
    return x,primo
          