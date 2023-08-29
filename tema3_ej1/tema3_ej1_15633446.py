# completa el código de la función
def suma_divisores(a):
    suma= 0
    for i in range(1,a):
        r=a%i
        if(r==0):
            suma+=i
    if(suma==1):
        u=True
    else:
        u=False
    return(suma,u)