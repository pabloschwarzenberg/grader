def suma_divisores(a):
    divisores=[]

    for i in range(2,a+1):
        if a%i==0:
            divisores.append(i)
            if sum(divisores)==1:
                return(sum(divisores),str(True))
            else:
                return(sum(divisores),str(False))
