# completa el código de la función
def amigos(a,b):
    suma1=0
    suma2=0
    for x in range(1,a):
        if a%x==0:
            suma1=suma1+x
    for z in range(1,b):
        if b%z==0:
            suma2=suma2+z
    if suma1==b and suma2==a:
        return True
    else:
        return False 
 
           