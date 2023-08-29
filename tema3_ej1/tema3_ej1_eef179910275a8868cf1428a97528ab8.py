# completa el código de la función
def suma_divisores(a):
    divisores=0
    for i in range(1,a):
        if a%i==0:
            divisores+=i
    if divisores==1:
        return(divisores,True)
    else:
        return(divisores,False)  