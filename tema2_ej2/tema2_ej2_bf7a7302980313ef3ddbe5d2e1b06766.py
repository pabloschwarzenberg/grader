def amigos(a,b):
    c=1
    suma_a=0
    while (c<a):
        if a%c==0:
            suma_a=suma_a+c
        c=c+1   
    c=1
    suma_b=0
    while (c<b):
        if b%c==0:
            suma_b=suma_b+c
        c=c+1
    
    if(suma_a == b and suma_b == a):
        return True
    else:
        return False