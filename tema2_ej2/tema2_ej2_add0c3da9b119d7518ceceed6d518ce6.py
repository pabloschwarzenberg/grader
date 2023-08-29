# completa el código de la función
def amigos(x,z):
    suma_x=0
    suma_z=0
    for i in range(1,x):
        if x%i==0:
            suma_x+=i
 
    for k in range(1,z):
        if z%k==0:
            suma_z+=k
    
    return suma_x==z and suma_z==x
    if suma_x == z and suma_z == x:
        return True
    else:
        return False 