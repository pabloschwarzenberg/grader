# completa el código de la función
def suma_divisores(a):
    divisores = []
    
    for i in range(1,a):
        if a%i==0:
            divisores.append(i)
    X=sum(divisores)
    Z=False
    if X ==1:
        Z=True        
    return (X,Z)
           