# completa el código de la función
def amigos(a,b):
    a1=[]
    b1=[]
    for x in range (1,a):
        if a % x == 0:
            a1.append(x)       
    for x in range (1,b):
        if b % x == 0:
            b1.append(x)
    if sum(a1)==b and sum(b1)==a:
        return True

    else:
        return False