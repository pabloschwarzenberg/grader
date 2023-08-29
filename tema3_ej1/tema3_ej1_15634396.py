def suma_divisores(numero):
    qwerty=numero
    a=1
    c=0
    while a<qwerty:
        b=qwerty%a
        if b==0:
            c=c+a
            a=a+1
            
        else:
            c=c
            a=a+1
    
    if c==1:
        return c,True
    
    else:
        return c,False