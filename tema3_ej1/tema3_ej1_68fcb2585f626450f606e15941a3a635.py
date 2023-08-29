# completa el código de la función
def suma_divisores(a):
    if a==1:
        return(0,False)
    x=0
    for i in range(1, a):
        if a% i == 0:
            x=x+i
    if a<2:    
        return False
    for i in range(2, a):
        if a % i == 0:
            return (x,False) 
    return (x,True)

