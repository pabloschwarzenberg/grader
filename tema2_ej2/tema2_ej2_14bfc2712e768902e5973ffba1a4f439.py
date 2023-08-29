# completa el código de la función
def amigos(a, b):
    a1=0
    b1=0
    for f in range (a-1):
        if a%(f+1)==0:
            a1+=(f+1)
    for j in range(b-1):
        if b % (j+1)==0:
            b1+=(j+1)
    if a1==b and b1==a:
        return True
    else:
        return False
        
amigos(220, 284)
           