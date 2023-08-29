# completa el código de la función
def amigos(a,b):
    divisor_suma=0
    divisor_sumab=0
    for x in range (1,a): 
        if a % x == 0: 
           divisor_suma+=x
    for y in range (1,b): 
        if b % y == 0: 
            divisor_sumab+=y
    if divisor_suma==b and divisor_sumab==a: 
        return True
    else:
         return False