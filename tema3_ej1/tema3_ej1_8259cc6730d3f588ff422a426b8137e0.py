# completa el código de la función
def suma_divisores(a):
    divisores=[]
    i=1
    while i<a:
        if a%i==0:
            divisores.append(i)
            i+=1
        else:
            i+=1
    if sum(divisores)==1:
        return (sum(divisores),True)
    else:
        return (sum(divisores),False)