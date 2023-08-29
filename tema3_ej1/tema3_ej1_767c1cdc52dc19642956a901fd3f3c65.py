def suma_divisores(x):
    divisores=[0]
    s=0
    for i in range(1,x):
        if x%i==0:
            divisores.append(i)
    for i in range(0,len(divisores)):
        s=divisores[i]+s
    if s==1:
        return 1,True
    else:
        return s,False

           