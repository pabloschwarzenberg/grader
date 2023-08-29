def numero_perfecto(a):
    x=1
    cont=0
    while x<a:
        
        if a%x==0:
            cont=cont+x
        x=x+1
    if cont==a:
        return True
    else:
        return False
           