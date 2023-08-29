def suma_divisores(a):
    prim= False
    divisor=[]
    for i in range(1, a-1):
        if a % i ==0:
            divisor.append(i)            
    div=sum(divisor)

    if div==1:
        prim=True
    return (div,prim)