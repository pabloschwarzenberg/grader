# completa el código de la función
def amigos(a,b):
    divisores_a=[]
    divisores_b=[]
    suma1=0
    suma2=0
    for i in range(1,a):
        if int(a)%i==0:
            divisores_a.append(i)
    for i in range(1,b):
        if int(b)%i==0:
            divisores_b.append(i)
    for x in divisores_a:
        suma1=suma1+x
    for y in divisores_b:
        suma2=suma2+y
    if suma1==b and suma2==a:
        sonamigos=True
    else:
        sonamigos=False
    return sonamigos

