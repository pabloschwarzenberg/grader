# completa el código de la función
def amigos(a,b):
    David=0
    John=0
    for i in range(1,a):
        if a%i==0:
            David +=i
 
    for k in range(1,b):
        if b%k==0:
            John +=k
 
    return David == b and John == a