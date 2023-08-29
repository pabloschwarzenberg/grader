# completa el código de la función
def suma_divisores(a):
    divisores=[]
    for i in range(1,a):
        if a%i==0:
            divisores.append(i)
    b=sum(divisores)
    if b==1:
        c=True
    else:
        c=False
    return b,c

