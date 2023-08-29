# completa el código de la función
#numeros amigos
def amigos(a,b):
    s_a=0
    s_b=0
    for i in range(1,a):
        if a%i==0:
            s_a+=i
    for x in range(1,b):
        if b%x==0:
            s_b+=x
    return s_a==b and s_b==a         