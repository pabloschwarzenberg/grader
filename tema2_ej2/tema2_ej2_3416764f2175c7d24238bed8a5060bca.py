def amigos(a,b):
    
    x=1
    cont=0
    
    while x<a:
        
        if a%x==0:
            cont=cont+x
        x=x+1
        
    y=1
    cont2=0
    
    while y<b:
        
        if b%y==0:
            cont2=cont2+y
        y=y+1

    print(cont)
    print(cont2)
            
    if cont==b and cont2==a:
        return True

    if cont!=b or cont2!=a:
        return False