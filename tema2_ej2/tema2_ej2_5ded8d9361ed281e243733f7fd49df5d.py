# completa el código de la función
def amigos(a,b):
    if a == b:
        return False
    elif a == 1 or a == 0 or b ==1 or b == 0:
        return False
    for divisor_a in range(1,(a-1)):
        div_a=0
        if a %divisor_a ==0 :
            div_a+=a
                
    for divisor_b in range (1,(b-1)):
        div_b=0
        if b % divisor_b == 0:
            div_b +=b
            
    if div_a == div_b:
        return True
    else:
        return False
