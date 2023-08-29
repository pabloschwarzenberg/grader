# completa el código de la función
def amigos(a,b):
    sum_a = 0
    sum_b = 0
    for n in range(1,a):
        
        if a % n == 0:
            sum_a += n

    for i in range(1,b):
        
        if b % i == 0:
            sum_b += i
            
    if sum_a == b and sum_b == a:
        return True
    else:
        return False
           