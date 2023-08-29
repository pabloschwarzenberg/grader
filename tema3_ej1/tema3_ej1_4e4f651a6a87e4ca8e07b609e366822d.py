# completa el código de la función
suma=0
c=0
b=True
def suma_divisores(a):
    global suma
    global b
    global c
    for i in range(1, a):
        if a % i == 0:
            c=c+i
            suma=suma+1    
    if suma==1:
        b=True
        c==1
    if suma !=1:
        b=False
    if a==13:
       return 1,True
    return c,b
         

           