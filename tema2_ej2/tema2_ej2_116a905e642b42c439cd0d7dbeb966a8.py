# completa el código de la función
def amigos(a,b):
    sumA=0
    sumB=0
    for divisor in range(1,a+1):
        if (a % divisor) == 0 :
            sumA=sumA+divisor
    for divisor in range(1,b+1):
        if (b % divisor) == 0 :
            sumB=sumB+divisor    
    if a==b:
        return False
    elif sumA==sumB:
        return True    
    else:
        return False