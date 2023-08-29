def suma_divisores(n):
    esprimo=True
    if n==1:
        return 0,False

    for i in range (2,n):
        if n%i==0:
            esprimo=False
    suma=0
    divisor=n
    while divisor>1:
        divisor=divisor-1
        if (n%divisor)==0:
            suma+=divisor
    return suma,esprimo   
    
