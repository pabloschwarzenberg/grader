# completa el código de la función
def amigos(a,b):
    x=0
    for i in range(1,a):
        if a%i==0:
            x= x+i
    y=0
    for i in range(1,b):
        if b%i==0:
            y= y+i
            
    if x==b and y==a and a!=b:
        return True
    else:
        return False