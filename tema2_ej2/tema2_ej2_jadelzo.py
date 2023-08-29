# completa el código de la función
def sumaamigos(a): 
    suma = 0 
 
    for i in range(1,a): 
        if a % i == 0: 
            suma += i 
    return suma


def sumaamigos2(b): 
    suma2 = 0 
 
    for j in range(1,b): 
        if b % j == 0: 
            suma2 += j 
    return suma2

def amigos(a,b):
    if sumaamigos(a)== b and sumaamigos2(b)==a:
        return True
    else:
        return False
           