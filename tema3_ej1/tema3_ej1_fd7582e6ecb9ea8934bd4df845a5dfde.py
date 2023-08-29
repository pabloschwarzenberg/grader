def suma_divisores(a):
    divisores=[1]
    if a==1:
        return (0,False)
    for i in range(2,a + 1) :
        if (a%i==0) and(i!=a) :
            divisores.append(i)
    if sum(divisores)==1:
            
        return sum(divisores),True
    else:
        return sum(divisores),False
       