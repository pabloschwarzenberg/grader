# completa el código de la función
def amigos(a,b):
    divisores_a=1
    divisores_b=1
    for m in range(2,a):
        if a%m==0:
            divisores_a=divisores_a+m
    for f in range(2,b):
        if b%f==0:
            divisores_b=divisores_b+f
    if a==2 or b==2:
        if a==2:
            divisores_a=divisores_a+2
        if b==2:
            divisores_b=divisores_b+2
    if divisores_a==b or divisores_b==a:
        return (True)
    else:
        return(False)
