# completa el código de la función
def suma_divisores(a):
    s=0
    for i in range(1,a):
        if a%i==0:
            s+=i
    return (s,s==1)

           