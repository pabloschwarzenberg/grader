# completa el código de la función

def amigos(a,b):
    sumaA = 0
    sumaB = 0
    
    for n in range(1,a):
        if a % n == 0:
            sumaA += n
            
    for m in range(1,b):
        if b % m == 0:
            sumaB += m
    if sumaA == b and sumaB == a:
        return True
    else:
        return False
            