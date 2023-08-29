# completa el código de la función
def suma_divisores(a):
    divisores=[]

    for i in range(1,a+1):
        if a%i==0:
            if i!=a:
                 divisores.append(i)
    if a==1:
        return sum(divisores),False
    elif a==2:
        return sum(divisores),True
    else:
        for j in range(2,a):
            if a%j==0:
                return sum(divisores),False
        return sum(divisores),True
    
           