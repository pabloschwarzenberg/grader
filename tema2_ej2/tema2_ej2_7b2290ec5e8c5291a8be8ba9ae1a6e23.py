# completa el código de la función
def amigos(a,b):
    counter_a = 0
    counter_b = 0
    for i in range( 1, int(a/2)+1 ):
        if a % i == 0:
            counter_a = counter_a + i
    for x in range( 1, int(b/2)+1 ):
        if b % x == 0:
            counter_b = counter_b + x
    
    if a == counter_b and b == counter_a:
        return True
    else:
        return False
           