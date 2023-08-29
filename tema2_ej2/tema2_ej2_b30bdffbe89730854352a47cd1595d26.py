# completa el código de la función
def amigos(a,b):
    sumaB=0
    sumaA=0
    for i in range(b-1):
        if b%(i+1)==0:
            sumaB=sumaB+(i+1)            
    for j in range(a-1):
        if a%(j+1)==0:
            sumaA=sumaA+(j+1)    
    if a==sumaB and b==sumaA:
        return(True)
    return(False)
           