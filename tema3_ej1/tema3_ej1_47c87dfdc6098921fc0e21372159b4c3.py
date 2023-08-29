def suma_divisores(n):
    primos=0
    v=True
    for i in range (1,n):
        if n % i ==0:
            primos = primos + i
            print (i)
    if(primos)==1:
       v=True
    else:
        v=False
    return (primos,v)
x=int()
suma_divisores(x)    