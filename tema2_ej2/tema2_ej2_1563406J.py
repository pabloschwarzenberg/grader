# completa el código de la función
def amigos(a,b):
    x=0
    z=0
    for i in range(1,a):
        if a%i==0:
            x=x+i
    for e in range(1,b):
        if b%e==0:
            z=z+e
    if x==b and z==a:
        return True 
    else:
        return False
