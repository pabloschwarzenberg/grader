def amigos(a,b):
    divisores_a=0
    for i in range(1,a):
        r=a%i
        if(r==0):
            divisores_a = divisores_a + i
        else:
            divisores_a=divisores_a
    divisores_b=0
    for k in range(1,b):
        l=b%k
        if(l==0):
            divisores_b = divisores_b + k
        else:
            divisores_b =divisores_b
    if (divisores_b==a)and (divisores_a==b):
        u=True
    else:
        u=False
    return(u)
           