# completa el código de la función
def amigos(a,b):
    suma_a=0
    suma_b=0
    for x in range(1,a):
        if a%x==0:
            suma_a+=x
 
    for y in range(1,b):
        if b%y==0:
            suma_b+=y
            
    return suma_a==b and suma_b==a          