# completa el código de la función
def suma_divisores(a):
    divisor=[1]
    if a==1:
        return(0,False)
    for i in range(2, a):
        if (a % i)==0:
            divisor.append(i)
    divisor=sum(divisor)
    if divisor==1:
        return(divisor,True)
    else:
        return(divisor,False)