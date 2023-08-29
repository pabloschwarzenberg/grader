def suma_divisores(n):
    divisores=0
    if n==1:
        return(divisores,False)
    for i in range (1 , n+1):
        if n%i==0 and i!=n:
            divisores=divisores+(i)
    if divisores > 1:
        return (divisores, False) 
    elif divisores ==1:
        return(divisores, True)