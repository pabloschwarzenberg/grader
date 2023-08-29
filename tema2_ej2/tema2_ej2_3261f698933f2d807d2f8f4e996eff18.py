# completa el código de la función
def amigos(a,b):
    suma1=0
    suma2=0
    
    for i in range(1,a):
        if a % i == 0:
            suma1 += i
 
    for c in range(1,b):
        if b % c == 0:
            suma2 += c

    return suma1 == b and suma2 == a
    if suma1 == b and suma2 == a:
        return True
    else:
        return False