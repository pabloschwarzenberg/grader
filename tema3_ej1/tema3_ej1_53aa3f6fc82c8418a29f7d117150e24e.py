def suma_divisores(x):
    divisores = [0]

    for i in range(1,x-1):
        if x % i==0:
            divisores.append(i)
    s = sum(divisores)
    if s==1:
       return (s,True)
    else:
        return (s,False)
