# completa el código de la función
def suma_divisores(a):
   
    x=1
    cont=0
    
    while x<a:
        
        if a%x==0:
            cont=cont+x
        x=x+1
        
    if (a%2!=0 and a!=1) or a==2:
        return (cont,True)
    else:
       return (cont,False)



           