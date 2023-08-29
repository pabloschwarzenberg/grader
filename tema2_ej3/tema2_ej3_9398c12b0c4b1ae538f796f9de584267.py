def numero_perfecto(a):
    b=1
    c=0
    while b<a:
        if a/b%1==0:
            c=c+b
        b=b+1
    if c==a:
        return True
    if c!=a:
        return False


    
    
           