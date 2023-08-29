# completa el código de la función
def amigos(a,b):
    divsuma=0
    divsumb=0
    for i in range(1,a):
        div=0
        if a%i==0:
            div=a//i
            divsuma+=div
        else:
            divsuma+=0
    divsuma-=a
    divsuma+=1
    for i in range(1,b):
        div=0
        if b%i==0:
            div=b//i
            divsumb+=div
        else:
            divsumb+=0
    divsumb-=b
    divsumb+=1
    if divsuma==b and divsumb==a:
        return True
    else:
        return False
           