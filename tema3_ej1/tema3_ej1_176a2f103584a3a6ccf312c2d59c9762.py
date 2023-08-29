def suma_divisores(a):
    divisor=[i for i in range(1,a) if a%i==0]
    m=sum(divisor)
    if m==1:
        return m,True
    return m,False