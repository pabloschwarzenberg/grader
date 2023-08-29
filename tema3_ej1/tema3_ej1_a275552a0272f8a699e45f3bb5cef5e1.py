# completa el código de la función
def suma_divisores(a):
    divisor=[]
    i=1
    while i<a:
        if a%i==0:
            divisor.append(i)
            i+=1
        else:
            i+=1
    if sum(divisor)==1:
        return (sum(divisor),True)
    else:
        return (sum(divisor),False)