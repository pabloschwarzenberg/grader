# completa el código de la función
def amigos(a,b):
    amigos=False
    divisores_a=0
    divisores_b=0
    for i in range (1,a-1):
        if a%i==0:
            divisores_a=divisores_a+i
    for l in range (1,b-1):
        if b%l==0:
            divisores_b=divisores_b+l
    if divisores_a==b and divisores_b==a:
        amigos=True
    return amigos