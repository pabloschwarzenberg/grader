# completa el código de la función
def suma_divisores(a):
    divisores=0
    for n in range(1,a-1):
        if a%n==0:
           divisores=divisores+n
        else:
            n!=divisores
    
    if divisores==1:
        return divisores,True
    elif divisores==0:
        return divisores,False
    else:
        return divisores,False
