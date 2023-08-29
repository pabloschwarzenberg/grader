# completa el código de la función
def amigos(a,b):
    divisor_a=1
    divisor_b=1
    for d in range(2,a):
        if a%d==0:
            divisor_a=divisor_a+d
    for f in range(2,b):
        if b%f==0:
            divisor_b=divisor_b+f
    if a==2 or b==2:
        if a==2:
            divisor_a=divisor_a+2
        if b==2:
            divisor_b=divisor_b+2
    if divisor_a==b or divisor_b==a:
        return (True)
    else:
        return(False) 