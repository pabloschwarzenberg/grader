# completa el código de la función
def amigos(a,b):
    c=1
    d=0
    for i in range(a-1) :
        if a%c==0 :
            d=d+c
        c+=1
    e=1
    f=0
    for i in range(b-1) :
        if b%e==0 :
            f=f+e
        e+=1

    if d==b and f==a :    
        return True
    else :
        return False
           