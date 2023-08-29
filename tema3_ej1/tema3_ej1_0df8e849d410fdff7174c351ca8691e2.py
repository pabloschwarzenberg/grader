def suma_divisores(a):
    divi=[i for i in range(1,a) if a%i==0]
    m=sum(divi)
    if m==1:
        return m,True
    return m,False

           