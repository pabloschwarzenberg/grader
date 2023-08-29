def suma_divisores(a):
    divisores=[]
    for i in range(1, a):
        if a%i==0:
            divisores.append(i)
    if sum(divisores)==1:
        return sum(divisores),True
    else:
        return sum(divisores),False
           