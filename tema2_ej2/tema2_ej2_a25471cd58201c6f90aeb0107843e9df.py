# completa el código de la función
def amigos(a,b):
    suma=0
    sumb=0
    for i in range(1,a):
        if a%i==0:
            suma +=i
 
    for k in range(1,b):
        if b%k==0:
            sumb +=k
 
    return suma == b and sumb == a
           