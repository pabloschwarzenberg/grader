def suma_divisores(a):
    total=0
    divisores=[]
    for i in range (1,a):
        if a%i == 0:
            divisores.append(i)
    for j in divisores:
        total=total+j
    if total == 1:
        return(total,True)
    return(total,False)