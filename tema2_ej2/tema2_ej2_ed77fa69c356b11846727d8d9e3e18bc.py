# completa el código de la función
def amigos(a,b):
    divisora=0
    divisorb=0
    for n in range(1,a):
        if a%n==0:
            divisora = divisora + n

    for m in range(1,b):
        if b % m == 0:
            divisorb = divisorb + m

    if divisora == b and divisorb == a:
        return True

    else:
        return False
      
            
        