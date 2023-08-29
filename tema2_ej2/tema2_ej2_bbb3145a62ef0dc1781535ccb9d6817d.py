# completa el código de la función
def amigos(a,b):
    s_a=0
    s_b=0
    for A in range(1,a):
        if a%A==0:
            s_a+=A
 
    for B in range(1,b):
        if b%B==0:
            s_b+=B
    
    return s_a==b and s_b == a
    if s_a == b and s_b == a:
        return True
    else:
        return False