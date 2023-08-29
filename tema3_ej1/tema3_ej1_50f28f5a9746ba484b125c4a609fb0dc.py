# completa el código de la función
def suma_divisores(num):
    sum=0
    for i in range(1, num):
        if num%i==0:
            sum+=i
    prim=sum==1
    return sum, prim  