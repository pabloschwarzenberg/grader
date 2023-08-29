# completa el código de la función
def suma_divisores(a):
    n=1
    divisores=0
    while n<a:
        if a%n==0:
            divisores+=n
            n+=1
        else:
            n+=1
    if divisores==1:
        primo=True
    else:
        primo=False
    return divisores,primo
           