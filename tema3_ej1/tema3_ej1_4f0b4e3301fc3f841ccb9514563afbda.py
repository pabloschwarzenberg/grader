def suma_divisores(n):
    divisores=[1]
    for i in range(2,n+1):
        if n%i==0:
            divisores.append(i)
    if n in divisores:
        divisores.remove(n)
    if sum(divisores)==1:
        resp=True
    else:
        contador=0
        resp=True
        for i in range(1,n+1):
            if (n%i==0):
                contador+=1
            if(contador>2) or n==1:
                resp=False

    return sum(divisores),resp
