# por favor escribe aquí tu función

def es_primo(numero):

    a=1
    a=int(a)
    b=2
    b=int(b)

    while b<numero and a!=0:

        a=numero%b       
        
        if a!=0:
        
            b=b+1

    if a==0 or numero==1:
        return False
    if a!=0:
        return True
    
    
    






           